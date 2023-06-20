import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/core/controllers/rewards_controller.dart';
import 'package:cpmms/src/features/core/models/rewards_model.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';
import 'package:flutter/services.dart';

class AddRewardsScreen extends StatelessWidget {
  const AddRewardsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final _formKey = GlobalKey<FormState>();
    final controller = Get.put(RewardsController());

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
          "Add New Voucher",
          style: Theme.of(context).textTheme.headlineMedium,
        ),
        centerTitle: true,
        elevation: 0,
        backgroundColor: Colors.transparent,
      ),
      body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.all(tDefaultSize),
          child: Column(
            children: [
              const SizedBox(height: 10),
              Form(
                key: _formKey,
                child: Column(
                  children: [
                    Stack(children: [
                      SizedBox(
                        width: 120,
                        height: 120,
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(100),
                          child: Image.asset(tDefaultPfp),
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
                            width: 35,
                            height: 35,
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(100),
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
                      controller: controller.rewardsTitle,
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return 'Please enter a value';
                        }
                        return null; // Return null if the input is valid
                      },
                      decoration: InputDecoration(
                        label: const Text("Voucher Title"),
                        border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(100)),
                        focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(100),
                            borderSide: const BorderSide(
                                width: 2, color: tSecondaryColor)),
                        prefixIcon: const Icon(LineAwesomeIcons.tags),
                      ),
                    ),
                    const SizedBox(height: tFormHeight - 20),
                    TextFormField(
                      controller: controller.rewardsInstruction,
                      maxLines: null,
                      decoration: InputDecoration(
                        label: const Text("Redeem Voucher Instruction Details"),
                        border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(100)),
                        focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(100),
                            borderSide: const BorderSide(
                                width: 2, color: tSecondaryColor)),
                        prefixIcon:
                            const Icon(LineAwesomeIcons.alternate_pencil),
                      ),
                    ),
                    const SizedBox(height: tFormHeight - 20),
                    TextFormField(
                      inputFormatters: [FilteringTextInputFormatter.digitsOnly],
                      controller: controller.rewardsCost,
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return 'Please enter a value';
                        }
                        return null; // Return null if the input is valid
                      },
                      decoration: InputDecoration(
                        label: const Text("Redeem Cost in Points"),
                        border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(100)),
                        focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(100),
                            borderSide: const BorderSide(
                                width: 2, color: tSecondaryColor)),
                        prefixIcon: const Icon(LineAwesomeIcons.coins),
                      ),
                    ),
                    const SizedBox(height: tFormHeight),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton(
                        onPressed: () async {
                          if (_formKey.currentState!.validate()) {
                            final reward = RewardsModel(
                                id: "temp",
                                cost: int.parse(
                                    controller.rewardsCost.text.trim()),
                                details: controller.rewardsTitle.text.trim(),
                                instruction:
                                    controller.rewardsInstruction.text.trim(),
                                img: "rewards/rewardID.jpg");

                            await controller.createReward(reward);
                          }
                        },
                        style: ElevatedButton.styleFrom(
                            backgroundColor: tPrimaryColor,
                            side: BorderSide.none,
                            shape: const StadiumBorder()),
                        child: const Text(
                          "Add Promotion",
                          style: TextStyle(color: tDarkColor),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
