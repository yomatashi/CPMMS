import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/authentications/models/admin_model.dart';
import 'package:cpmms/src/features/core/controllers/nav_controller.dart';
import 'package:cpmms/src/features/core/controllers/profile_controller.dart';
import 'package:cpmms/src/features/core/controllers/promotion_controller.dart';
import 'package:cpmms/src/features/core/controllers/rewards_controller.dart';
import 'package:cpmms/src/features/core/screens/promotion/promotion_admin.dart';
import 'package:cpmms/src/features/core/screens/rewards/rewards_admin.dart';
import 'package:cpmms/src/features/widget/circular_button/circular_btn.dart';
import 'package:cpmms/src/features/widget/nav_sidebar/nav_sidebar_admin.dart';
import 'package:cpmms/src/features/core/screens/profile/profile_screen.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';

class DashboardAdmin extends StatelessWidget {
  const DashboardAdmin({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    Get.put(NavigationController());
    final controller = Get.put(ProfileController());
    controller.getAdminDataFuture();
    final promotionController = Get.put(PromotionController());
    promotionController.getPromotionList();
    final rewardsController = Get.put(RewardsController());
    rewardsController.getRewardsList();
    return Scaffold(
      appBar: AppBar(
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
                Get.to(() => const ProfileScreen(role: "Admin"));
              },
              icon: const Icon(Icons.person_2_outlined, color: Colors.black54),
            ),
          ),
        ],
      ),
      drawer: SidebarAdmin(),
      body: SingleChildScrollView(
        child: Container(
            padding: const EdgeInsets.all(tDashboardPadding),
            child: Obx(() {
              AdminModel adminData = controller.adminData.value;
              return Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Hey, ${adminData.fullName}",
                    style: txtTheme.bodyLarge?.apply(fontSizeFactor: 1.1),
                  ),
                  const SizedBox(height: 15),
                  Center(
                    child: SizedBox(
                      height: 100,
                      child: ListView(
                        scrollDirection: Axis.horizontal,
                        children: <Widget>[
                          CircularButton(
                              icon: LineAwesomeIcons.gift,
                              text: "Rewards Manager",
                              onPressed: () {
                                rewardsController.isLoading.value = true;
                                rewardsController.isLoading2.value = true;
                                Get.to(() => const RewardsManager(),
                                    transition: Transition.fadeIn);
                              }),
                          CircularButton(
                              icon: LineAwesomeIcons.tags,
                              text: "Promotion Manager",
                              onPressed: () {
                                promotionController.isLoading.value = true;
                                Get.to(() => const PromotionManager(),
                                    transition: Transition.fadeIn);
                              }),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(height: 10),
                  Text(
                    "Promotions",
                    style: txtTheme.headlineLarge,
                  ),
                  const SizedBox(height: 10),
                  SizedBox(
                    height: 450,
                    child: promotionController.isLoading.value == false
                        ? ListView.builder(
                            shrinkWrap: true,
                            scrollDirection: Axis.horizontal,
                            itemCount:
                                promotionController.promotionData.value.length,
                            itemBuilder: (context, index) {
                              final promo = promotionController
                                  .promotionData.value[index];
                              return SizedBox(
                                width: 340,
                                height: 210,
                                child: Padding(
                                  padding:
                                      const EdgeInsets.only(right: 10, top: 5),
                                  child: Container(
                                    decoration: BoxDecoration(
                                        borderRadius: BorderRadius.circular(10),
                                        color: tCardBgColor),
                                    padding: const EdgeInsets.all(10),
                                    child: Column(
                                      crossAxisAlignment:
                                          CrossAxisAlignment.start,
                                      children: [
                                        Row(
                                          mainAxisAlignment:
                                              MainAxisAlignment.spaceBetween,
                                          children: [
                                            Flexible(
                                              child: Text(
                                                promo.promotionName,
                                                style: txtTheme.headlineSmall,
                                                maxLines: 2,
                                                overflow: TextOverflow.ellipsis,
                                              ),
                                            ),
                                          ],
                                        ),
                                        Row(
                                          children: [
                                            Flexible(
                                              child: promotionController
                                                          .imageUrl
                                                          .value[index] !=
                                                      "none"
                                                  ? Image.network(
                                                      promotionController
                                                          .imageUrl
                                                          .value[index],
                                                      height: 200)
                                                  : Image.asset(tLogoImage,
                                                      height: 200),
                                            ),
                                          ],
                                        ),
                                        Row(
                                          mainAxisAlignment:
                                              MainAxisAlignment.spaceBetween,
                                          children: [
                                            Flexible(
                                              child: Text(
                                                promo.details,
                                                style: txtTheme.bodyLarge,
                                                maxLines: 6,
                                                overflow: TextOverflow.ellipsis,
                                              ),
                                            ),
                                          ],
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              );
                            },
                          )
                        : const Center(
                            child: CircularProgressIndicator(),
                          ),
                  ),
                  const SizedBox(height: tDashboardPadding),
                ],
              );
            })),
      ),
    );
  }
}
