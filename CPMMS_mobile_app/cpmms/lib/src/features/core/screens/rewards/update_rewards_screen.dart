import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/core/controllers/rewards_controller.dart';
import 'package:cpmms/src/features/core/models/rewards_model.dart';
import 'package:flutter/material.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';
import 'package:get/get.dart';
import 'package:flutter/services.dart';

class UpdateRewardsScreen extends StatelessWidget {
  const UpdateRewardsScreen({required this.rewardsID, Key? key})
      : super(key: key);

  final String rewardsID;

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    final controller = Get.put(RewardsController());
    final _formKey = GlobalKey<FormState>();

    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            controller.isLoading.value = true;
            controller.isLoading2.value = true;
            controller.getRewardsList();
            Get.back();
          },
          icon: const Icon(LineAwesomeIcons.angle_left, color: Colors.black54),
        ),
        title: Text(
          "Edit Voucher",
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
            builder: ((Context, snapshot) {
              if (snapshot.connectionState == ConnectionState.done) {
                if (snapshot.hasData) {
                  RewardsModel rewardsData = snapshot.data as RewardsModel;
                  final details =
                      TextEditingController(text: rewardsData.details);
                  final instruction =
                      TextEditingController(text: rewardsData.instruction);
                  final cost =
                      TextEditingController(text: rewardsData.cost.toString());
                  return Obx(() {
                    if (controller.singleImageUrl.value != '') {
                      return Column(
                        children: [
                          const SizedBox(height: 10),
                          Form(
                            key: _formKey,
                            child: Column(
                              children: [
                                Stack(children: [
                                  SizedBox(
                                    width: 200,
                                    height: 200,
                                    child: ClipRRect(
                                      child: controller.singleImageUrl.value !=
                                              "none"
                                          ? Image.network(
                                              controller.singleImageUrl.value)
                                          : Image.asset(tLogoImage),
                                    ),
                                  ),
                                  Positioned(
                                    bottom: 0,
                                    right: 0,
                                    child: InkWell(
                                      onTap: () {
                                        controller.pickImage();
                                      },
                                      child: Container(
                                        width: 50,
                                        height: 50,
                                        decoration: BoxDecoration(
                                          borderRadius:
                                              BorderRadius.circular(100),
                                          color: tPrimaryColor,
                                        ),
                                        child: const Icon(
                                          LineAwesomeIcons.alternate_pencil,
                                          size: 20,
                                          color: Colors.black,
                                        ),
                                      ),
                                    ),
                                  )
                                ]),
                                const SizedBox(height: 50),
                                TextFormField(
                                  controller: details,
                                  validator: (value) {
                                    if (value == null || value.isEmpty) {
                                      return 'Please enter a value';
                                    }
                                    return null; // Return null if the input is valid
                                  },
                                  decoration: InputDecoration(
                                    label: const Text("Voucher Title"),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(100)),
                                    focusedBorder: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(100),
                                        borderSide: const BorderSide(
                                            width: 2, color: tSecondaryColor)),
                                    prefixIcon:
                                        const Icon(LineAwesomeIcons.tags),
                                  ),
                                ),
                                const SizedBox(height: tFormHeight - 20),
                                TextFormField(
                                  controller: instruction,
                                  maxLines: null,
                                  decoration: InputDecoration(
                                    label: const Text(
                                        "Redeem Voucher Instruction"),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(100)),
                                    focusedBorder: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(100),
                                        borderSide: const BorderSide(
                                            width: 2, color: tSecondaryColor)),
                                    prefixIcon: const Icon(
                                        LineAwesomeIcons.alternate_pencil),
                                  ),
                                ),
                                const SizedBox(height: tFormHeight - 20),
                                TextFormField(
                                  inputFormatters: [
                                    FilteringTextInputFormatter.digitsOnly
                                  ],
                                  controller: cost,
                                  validator: (value) {
                                    if (value == null || value.isEmpty) {
                                      return 'Please enter a value';
                                    }
                                    return null; // Return null if the input is valid
                                  },
                                  decoration: InputDecoration(
                                    label: const Text("Redeem Cost in Points"),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(100)),
                                    focusedBorder: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(100),
                                        borderSide: const BorderSide(
                                            width: 2, color: tSecondaryColor)),
                                    prefixIcon: const Icon(
                                        LineAwesomeIcons.coins),
                                  ),
                                ),
                                const SizedBox(height: tFormHeight),
                                SizedBox(
                                  width: double.infinity,
                                  child: ElevatedButton(
                                    onPressed: rewardsData.id ==
                                            "rPTW93zLm5QUQ7PWV20a"
                                        ? null
                                        : () async {
                                            if (_formKey.currentState!
                                                .validate()) {
                                              final newRewardData = RewardsModel(
                                                  id: rewardsData.id,
                                                  cost: int.parse(
                                                      cost.text.trim()),
                                                  details: details.text.trim(),
                                                  instruction:
                                                      instruction.text.trim(),
                                                  img: rewardsData.img != ""
                                                      ? rewardsData.img
                                                      : "rewards/${rewardsData.id}.jpg");

                                              await controller
                                                  .updateRewards(newRewardData);
                                            }
                                          },
                                    style: ElevatedButton.styleFrom(
                                        backgroundColor: tPrimaryColor,
                                        side: BorderSide.none,
                                        shape: const StadiumBorder()),
                                    child: const Text(
                                      "Update Promotion",
                                      style: TextStyle(color: tDarkColor),
                                    ),
                                  ),
                                ),
                                const SizedBox(height: tFormHeight - 20),
                                SizedBox(
                                  width: double.infinity,
                                  child: ElevatedButton(
                                    onPressed:
                                        rewardsData.id == "rPTW93zLm5QUQ7PWV20a"
                                            ? null
                                            : () async {
                                                await controller
                                                    .deleteRewards(rewardsData);
                                              },
                                    style: ElevatedButton.styleFrom(
                                        backgroundColor: Colors.redAccent,
                                        side: BorderSide.none,
                                        shape: const StadiumBorder()),
                                    child: const Text(
                                      "Delete Promotion",
                                      style: TextStyle(color: tDarkColor),
                                    ),
                                  ),
                                ),
                              ],
                            ),
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
      ),
    );
  }
}
