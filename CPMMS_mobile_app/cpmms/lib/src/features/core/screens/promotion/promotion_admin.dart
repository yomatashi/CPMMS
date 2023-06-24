import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/core/controllers/nav_controller.dart';
import 'package:cpmms/src/features/core/controllers/profile_controller.dart';
import 'package:cpmms/src/features/core/controllers/promotion_controller.dart';
import 'package:cpmms/src/features/core/screens/profile/profile_screen.dart';
import 'package:cpmms/src/features/core/screens/promotion/add_promotion_screen.dart';
import 'package:cpmms/src/features/core/screens/promotion/update_promotion_screen.dart';
import 'package:cpmms/src/features/widget/nav_sidebar/nav_sidebar_admin.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';

class PromotionManager extends StatelessWidget {
  const PromotionManager({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    Get.put(NavigationController());
    final controller = Get.put(ProfileController());
    controller.getAdminDataFuture();
    final promotionController = Get.put(PromotionController());
    promotionController.getPromotionList();
    var mediaQuery = MediaQuery.of(context);
    double height = mediaQuery.size.height;
    double width = mediaQuery.size.width;

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
          child: Obx(
            () {
              if (promotionController.isLoading.value == false) {
                return Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      "Active Promotions",
                      style: txtTheme.headlineMedium,
                    ),
                    const SizedBox(height: 10),
                    SizedBox(
                      height: height * 0.7,
                      child: ListView.builder(
                        shrinkWrap: true,
                        itemCount:
                            promotionController.promotionData.value.length,
                        itemBuilder: (context, index) {
                          final promo =
                              promotionController.promotionData.value[index];
                          return InkWell(
                            onTap: () {
                              Get.to(() => UpdatePromotionScreen(
                                  promoID: promotionController
                                      .promotionData.value[index].id));
                            },
                            child: ListTile(
                              contentPadding: const EdgeInsets.only(top: 10),
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
                                            style: txtTheme.headlineSmall),
                                      ],
                                    ),
                                  ),
                                  SizedBox(
                                    width: width * 0.35,
                                    child: promotionController
                                                .imageUrl.value[index] !=
                                            "none"
                                        ? Image.network(promotionController
                                            .imageUrl.value[index])
                                        : Image.asset(tLogoImage),
                                  ),
                                  SizedBox(width: width * 0.05),
                                  SizedBox(
                                    width: width * 0.55,
                                    child: Column(
                                      crossAxisAlignment:
                                          CrossAxisAlignment.start,
                                      children: [
                                        Text(promo.promotionName,
                                            style: txtTheme.headlineSmall),
                                      ],
                                    ),
                                  ),
                                ]),
                              ),
                            ),
                          );
                        },
                      ),
                    ),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton(
                        onPressed: () {
                          Get.to(() => const AddPromotionScreen());
                        },
                        style: ElevatedButton.styleFrom(
                            backgroundColor: tPrimaryColor,
                            side: BorderSide.none,
                            shape: const StadiumBorder()),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            const Icon(LineAwesomeIcons.plus,
                                color: tWhiteColor),
                            Text(
                              "Add New Promotion",
                              style:
                                  txtTheme.bodyLarge?.apply(color: tWhiteColor),
                            ),
                          ],
                        ),
                      ),
                    )
                  ],
                );
              } else {
                return const Center(child: CircularProgressIndicator());
              }
            },
          ),
        ),
      ),
    );
  }
}
