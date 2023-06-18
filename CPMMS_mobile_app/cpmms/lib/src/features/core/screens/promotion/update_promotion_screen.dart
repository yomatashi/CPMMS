import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/authentications/models/promotion_model.dart';
import 'package:cpmms/src/features/core/controllers/promotion_controller.dart';
import 'package:flutter/material.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';
import 'package:get/get.dart';

class UpdatePromotionScreen extends StatelessWidget {
  const UpdatePromotionScreen({required this.promoID, Key? key})
      : super(key: key);

  final String promoID;

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    final controller = Get.put(PromotionController());
    final _formKey = GlobalKey<FormState>();

    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            controller.isLoading.value = true;
            controller.getPromotionList();
            Get.back();
          },
          icon: const Icon(LineAwesomeIcons.angle_left, color: Colors.black54),
        ),
        title: Text(
          "Edit Promotion",
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
              future: controller.getPromoData(promoID),
              builder: ((context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  if (snapshot.hasData) {
                    PromotionModel promoData = snapshot.data as PromotionModel;
                    final promoName =
                        TextEditingController(text: promoData.promotionName);
                    final promoDetails =
                        TextEditingController(text: promoData.details);
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
                                    controller: promoName,
                                    validator: (value) {
                                      if (value == null || value.isEmpty) {
                                        return 'Please enter a value';
                                      }
                                      return null; // Return null if the input is valid
                                    },
                                    decoration: InputDecoration(
                                      label: const Text("Promotion Title"),
                                      border: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(100)),
                                      focusedBorder: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(100),
                                          borderSide: const BorderSide(
                                              width: 2,
                                              color: tSecondaryColor)),
                                      prefixIcon:
                                          const Icon(LineAwesomeIcons.tags),
                                    ),
                                  ),
                                  const SizedBox(height: tFormHeight - 20),
                                  TextFormField(
                                    controller: promoDetails,
                                    maxLines: null,
                                    decoration: InputDecoration(
                                      label: const Text("Promotion Details"),
                                      border: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(100)),
                                      focusedBorder: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(100),
                                          borderSide: const BorderSide(
                                              width: 2,
                                              color: tSecondaryColor)),
                                      prefixIcon: const Icon(
                                          LineAwesomeIcons.alternate_pencil),
                                    ),
                                  ),
                                  const SizedBox(height: tFormHeight),
                                  SizedBox(
                                    width: double.infinity,
                                    child: ElevatedButton(
                                      onPressed: () async {
                                        if (_formKey.currentState!.validate()) {
                                          final newPromodata = PromotionModel(
                                              id: promoData.id,
                                              promotionName:
                                                  promoName.text.trim(),
                                              details: promoDetails.text.trim(),
                                              img: promoData.img);

                                          await controller
                                              .updatePromo(newPromodata);
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
                                      onPressed: () async {
                                        await controller.deletePromotion(promoData);
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
            )),
      ),
    );
  }
}
