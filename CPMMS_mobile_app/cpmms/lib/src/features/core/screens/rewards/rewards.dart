import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/core/controllers/nav_controller.dart';
import 'package:cpmms/src/features/core/controllers/profile_controller.dart';
import 'package:cpmms/src/features/core/controllers/rewards_controller.dart';
import 'package:cpmms/src/features/core/models/claim_rewards_model.dart';
import 'package:cpmms/src/features/core/models/rewards_model.dart';
import 'package:cpmms/src/features/core/screens/profile/profile_screen.dart';
import 'package:cpmms/src/features/core/screens/rewards/claim_rewards.dart';
import 'package:cpmms/src/features/core/screens/rewards/rewards_data.dart';
import 'package:flutter/material.dart';
import 'package:cpmms/src/features/widget/nav_sidebar/nav_sidebar.dart';
import 'package:get/get.dart';
import 'package:cpmms/src/features/authentications/models/member_model.dart';

class Rewards extends StatelessWidget {
  const Rewards({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    Get.put(NavigationController());
    final controller = Get.put(ProfileController());
    controller.getMemberDataFuture();
    final rewardsController = Get.put(RewardsController());
    rewardsController.getRewardsList();
    var mediaQuery = MediaQuery.of(context);
    double height = mediaQuery.size.height;
    double width = mediaQuery.size.width;

    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          bottom: TabBar(
            indicatorColor: tPrimaryColor,
            tabs: [
              Tab(
                child: Text(
                  "DEALS",
                  style: txtTheme.bodyLarge
                      ?.apply(fontSizeFactor: 1.2, fontWeightDelta: 2),
                ),
              ),
              Tab(
                child: Text(
                  "MY VOUCHERS",
                  style: txtTheme.bodyLarge
                      ?.apply(fontSizeFactor: 1.2, fontWeightDelta: 2),
                ),
              ),
            ],
          ),
          leading: Builder(
            builder: (BuildContext context) {
              return IconButton(
                icon: const Icon(
                  Icons.menu,
                  color: Colors.black,
                ),
                onPressed: () {
                  Scaffold.of(context).openDrawer();
                },
              );
            },
          ),
          title: Text("Consult Pharmacy", style: txtTheme.headlineSmall?.apply(fontSizeFactor: 0.9)),
          centerTitle: true,
          elevation: 0,
          backgroundColor: Colors.transparent,
          actions: [
            Container(
              margin: const EdgeInsets.only(right: 20, top: 7),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                color: tCardBgColor,
              ),
              child: IconButton(
                onPressed: () {
                  Get.to(() => const ProfileScreen(role: "Member"));
                },
                icon:
                    const Icon(Icons.person_2_outlined, color: Colors.black54),
              ),
            ),
          ],
        ),
        drawer: Sidebar(),
        body: TabBarView(
          children: [
            TabView1(rewardsController: rewardsController, height: height),
            TabView2(controller: controller, rewardsController: rewardsController, height: height, width: width, txtTheme: txtTheme),
          ],
        ),
      ),
    );
  }
}

class TabView2 extends StatelessWidget {
  const TabView2({
    super.key,
    required this.controller,
    required this.rewardsController,
    required this.height,
    required this.width,
    required this.txtTheme,
  });

  final ProfileController controller;
  final RewardsController rewardsController;
  final double height;
  final double width;
  final TextTheme txtTheme;

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Container(
        padding: const EdgeInsets.all(tDashboardPadding),
        child: Obx(() {
          MemberModel memberData = controller.memberData.value;
          rewardsController.getClaimRewardsList(memberData.id);
          List<ClaimRewardsModel> claimRwrd =
              rewardsController.claimRewardsData.value;
          List<RewardsModel> currRewards =
              rewardsController.claimRewardsDetails.value;
          List<String> imgURL =
              rewardsController.imgURLforClaimRwrd.value;
          if (rewardsController.isLoading2.value == false) {
            return Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(
                    height: height,
                    child: ListView.builder(
                      shrinkWrap: true,
                      itemCount: claimRwrd.length,
                      itemBuilder: (context, index) {
                        // if (rewardsController.singleImageUrl.value !=
                        // '') {
                        return InkWell(
                          onTap: () {
                            Get.to(() => ClaimRewardsScreen(imgURL: imgURL[index], details: currRewards[index].details, instruction: currRewards[index].instruction, claimRewardsID: claimRwrd[index].id));
                          },
                          child: ListTile(
                            contentPadding: const EdgeInsets.all(0),
                            title: FittedBox(
                              fit: BoxFit.scaleDown,
                              child: Row(children: [
                                SizedBox(
                                  width: width * 0.05,
                                  child: Column(
                                    crossAxisAlignment:
                                        CrossAxisAlignment.start,
                                    children: [
                                      Text((index + 1).toString(),
                                          style:
                                              txtTheme.headlineSmall),
                                    ],
                                  ),
                                ),
                                SizedBox(
                                  width: width * 0.35,
                                  child: imgURL[index] != "none"
                                      ? Image.network(imgURL[index])
                                      : Image.asset(tLogoImage),
                                ),
                                SizedBox(width: width * 0.05),
                                SizedBox(
                                  width: width * 0.55,
                                  child: Column(
                                    crossAxisAlignment:
                                        CrossAxisAlignment.start,
                                    children: [
                                      Text(
                                        currRewards[index].details,
                                        style: txtTheme.headlineSmall,
                                        maxLines: 2,
                                        overflow: TextOverflow.ellipsis,
                                      ),
                                    ],
                                  ),
                                ),
                              ]),
                            ),
                          ),
                        );
                        // } else {
                        //   return const Center(
                        //       child: CircularProgressIndicator());
                        // }
                      },
                    ))
              ],
            );
          } else {
            return const Center(child: CircularProgressIndicator());
          }
        }),
      ),
    );
  }
}

class TabView1 extends StatelessWidget {
  const TabView1({
    super.key,
    required this.rewardsController,
    required this.height,
  });

  final RewardsController rewardsController;
  final double height;

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Container(
        padding: const EdgeInsets.all(tDashboardPadding),
        child: Obx(() {
          List<RewardsModel> rewardsData = rewardsController.rewardsData.value;
          if (rewardsController.isLoading.value == false) {
            return Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(
                  height: height,
                  child: GridView.count(
                    crossAxisSpacing: 10,
                    mainAxisSpacing: 10,
                    crossAxisCount: 2,
                    children: <Widget>[
                      for (int i = 0; i < rewardsData.length; i++)
                        InkWell(
                          onTap: () {
                            Get.to(() => RewardsDetailsScreen(
                                rewardsID: rewardsData[i].id));
                          },
                          child: Container(
                              padding: const EdgeInsets.all(0),
                              child: Column(
                                children: [
                                  SizedBox(
                                      height: 92,
                                      child:
                                          rewardsController.imageUrl.value[i] !=
                                                  "none"
                                              ? Image.network(rewardsController
                                                  .imageUrl.value[i])
                                              : Image.asset(tLogoImage)),
                                  Text(
                                    rewardsData[i].details,
                                    maxLines: 2,
                                    overflow: TextOverflow.ellipsis,
                                  ),
                                  Text("${rewardsData[i].cost.toString()}pts"),
                                ],
                              )),
                        ),
                    ],
                  ),
                ),
              ],
            );
          } else {
            return const Center(child: CircularProgressIndicator());
          }
        }),
      ),
    );
  }
}
