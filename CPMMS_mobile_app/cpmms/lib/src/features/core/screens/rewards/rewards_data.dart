import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/authentications/models/member_model.dart';
import 'package:cpmms/src/features/core/controllers/profile_controller.dart';
import 'package:cpmms/src/features/core/controllers/rewards_controller.dart';
import 'package:cpmms/src/features/core/models/claim_rewards_model.dart';
import 'package:cpmms/src/features/core/models/rewards_model.dart';
import 'package:flutter/material.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';
import 'package:get/get.dart';
import 'package:cpmms/src/constants/image_strings.dart';

class RewardsDetailsScreen extends StatelessWidget {
  const RewardsDetailsScreen({required this.rewardsID, Key? key})
      : super(key: key);

  final String rewardsID;

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    final controller = Get.put(RewardsController());
    final memberController = Get.put(ProfileController());
    memberController.getMemberDataFuture();
    return Scaffold(
        appBar: AppBar(
          leading: IconButton(
            onPressed: () {
              controller.isLoading.value = true;
              controller.getRewardsList();
              Get.back();
            },
            icon:
                const Icon(LineAwesomeIcons.angle_left, color: Colors.black54),
          ),
          title: Text(
            "Reward details",
            style: Theme.of(context).textTheme.headlineMedium,
          ),
          centerTitle: true,
          elevation: 0,
          backgroundColor: Colors.transparent,
        ),
        body: SingleChildScrollView(
          child: Container(
            padding: const EdgeInsets.all(tDefaultSize),
            child: FutureBuilder(
              future: controller.getRewardsData(rewardsID),
              builder: ((context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  if (snapshot.hasData) {
                    RewardsModel rewardsData = snapshot.data as RewardsModel;
                    return Obx(() {
                      if (controller.singleImageUrl.value != '') {
                        return Column(
                          children: [
                            const SizedBox(height: 10),
                            Column(
                              children: [
                                Stack(
                                  children: [
                                    SizedBox(
                                      width: 200,
                                      height: 200,
                                      child: ClipRRect(
                                        // borderRadius:
                                        //     BorderRadius.circular(100),
                                        child: controller
                                                    .singleImageUrl.value !=
                                                "none"
                                            ? Image.network(
                                                controller.singleImageUrl.value)
                                            : Image.asset(tLogoImage),
                                      ),
                                    ),
                                  ],
                                ),
                                Text("Cost: ${rewardsData.cost} pts", style: txtTheme.bodyLarge?.apply(fontSizeFactor: 1.2)),
                                const SizedBox(height: 40),
                                Text(rewardsData.details, style: txtTheme.headlineSmall),
                                const SizedBox(height: 10),
                                Text(rewardsData.instruction, style: txtTheme.bodyLarge),
                                const SizedBox(height: 20),
                                SizedBox(
                                  width: double.infinity,
                                  child: ElevatedButton(
                                    onPressed:
                                        rewardsID == "rPTW93zLm5QUQ7PWV20a"
                                            ? null
                                            : () async {
                                                final memberData = memberController.memberData.value;

                                                final claimReward = ClaimRewardsModel(id: "temp", claimStatus: false, memberID: memberData.id, rewardsID: rewardsID);

                                                final updateMember = MemberModel(id: memberData.id, fullName: memberData.fullName, email: memberData.email, IC: memberData.IC, points: (memberData.points - rewardsData.cost), pfp: memberData.pfp);

                                                await memberController.updateMemberNoSnackbar(updateMember, rewardsData);
                                                await controller.createClaimRewards(claimReward);
                                              },
                                    style: ElevatedButton.styleFrom(
                                        backgroundColor: tPrimaryColor,
                                        side: BorderSide.none,
                                        shape: const StadiumBorder()),
                                    child: const Text(
                                      "Redeem Voucher",
                                      style: TextStyle(color: tDarkColor),
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ],
                        );
                      } else {
                        return const Center(child: CircularProgressIndicator());
                      }
                    });
                  } else if (snapshot.hasError) {
                    return Center(child: Text(snapshot.error.toString()));
                  } else {
                    return const Center(child: Text("Something went wrong"));
                  }
                } else {
                  return const Center(child: CircularProgressIndicator());
                }
              }),
            ),
          ),
        ));
  }
}
