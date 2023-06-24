import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/authentications/models/promotion_model.dart';
import 'package:cpmms/src/features/core/controllers/promotion_controller.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';

class AddPromotionScreen extends StatelessWidget {
  const AddPromotionScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final _formKey = GlobalKey<FormState>();
    final controller = Get.put(PromotionController());

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
          "Add New Promotion",
          style: Theme.of(context).textTheme.headlineSmall?.apply(fontSizeFactor: 0.9),
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
                      controller: controller.promoName,
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return 'Please enter a value';
                        }
                        return null; // Return null if the input is valid
                      },
                      decoration: InputDecoration(
                        label: const Text("Promotion Title"),
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
                      controller: controller.promoDetails,
                      maxLines: null,
                      decoration: InputDecoration(
                        label: const Text("Promotion Details"),
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
                    const SizedBox(height: tFormHeight),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton(
                        onPressed: () async {
                          if (_formKey.currentState!.validate()) {
                            final promo = PromotionModel(id: "temp", promotionName: controller.promoName.text.trim(), details: controller.promoDetails.text.trim(), img: "promotion/promoID.jpg");

                            await controller.createPromotion(promo);
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
