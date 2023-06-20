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

class ClaimRewardsScreen extends StatelessWidget {
  const ClaimRewardsScreen(
      {required this.imgURL,
      required this.details,
      required this.instruction,
      required this.claimRewardsID,
      Key? key})
      : super(key: key);

  final String imgURL;
  final String details;
  final String instruction;
  final String claimRewardsID;

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    final controller = Get.put(RewardsController());
    // final memberController = Get.put(ProfileController());
    // memberController.getMemberDataFuture();
    return Scaffold(
        appBar: AppBar(
          leading: IconButton(
            onPressed: () {
              controller.isLoading.value = true;
              controller.isLoading2.value = true;
              controller.getRewardsList();
              Get.back();
            },
            icon:
                const Icon(LineAwesomeIcons.angle_left, color: Colors.black54),
          ),
          title: Text(
            "Claim reward",
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
              future: controller.getClaimRewardData(claimRewardsID),
              builder: ((context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  if (snapshot.hasData) {
                    ClaimRewardsModel claimRewardData =
                        snapshot.data as ClaimRewardsModel;
                    // return Obx(() {
                      controller.getClaimRewardData(claimRewardsID);
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
                                      child: imgURL != "none"
                                          ? Image.network(imgURL)
                                          : Image.asset(tLogoImage),
                                    ),
                                  ),
                                ],
                              ),
                              // Text("Cost: ${rewardsData.cost} pts",
                              //     style:
                              //         txtTheme.bodyLarge?.apply(fontSizeFactor: 1.2)),
                              const SizedBox(height: 50),
                              Text(details, style: txtTheme.headlineSmall),
                              const SizedBox(height: 10),
                              Text(instruction, style: txtTheme.bodyLarge),
                              const SizedBox(height: 20),
                              SizedBox(
                                width: double.infinity,
                                child: ElevatedButton(
                                  onPressed: claimRewardData.claimStatus == true
                                      ? null
                                      : () async {
                                          final newClaimRewardData = ClaimRewardsModel(id: claimRewardData.id, claimStatus: true, memberID: claimRewardData.memberID, rewardsID: claimRewardData.rewardsID);

                                          await controller.updateClaimReward(newClaimRewardData);
                                        },
                                  style: ElevatedButton.styleFrom(
                                      backgroundColor: tPrimaryColor,
                                      side: BorderSide.none,
                                      shape: const StadiumBorder()),
                                  child: claimRewardData.claimStatus == true
                                      ? const Text(
                                          "Voucher has already been claimed",
                                          style: TextStyle(color: tDarkColor),
                                        )
                                      : const Text(
                                          "Claim Voucher",
                                          style: TextStyle(color: tDarkColor),
                                        ),
                                ),
                              ),
                            ],
                          ),
                        ],
                      );
                    // });
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
