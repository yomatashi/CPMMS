import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/core/controllers/nav_controller.dart';
import 'package:cpmms/src/features/core/controllers/promotion_controller.dart';
import 'package:cpmms/src/features/widget/nav_sidebar/nav_sidebar_guest.dart';
import 'package:cpmms/src/repository/authentication_repository/authentication_repository.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class DashboardGuest extends StatelessWidget {
  const DashboardGuest({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    Get.put(NavigationController());
    final promotionController = Get.put(PromotionController());
    promotionController.getPromotionList();
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
        title: Text("Consult Pharmacy",
            style: Theme.of(context).textTheme.headlineMedium),
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
                AuthenticationRepository.instance.logout();
              },
              icon: const Icon(Icons.person_2_outlined, color: Colors.black54),
            ),
          ),
        ],
      ),
      drawer: SidebarGuest(),
      body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.all(tDashboardPadding),
          child: Obx(() {
            return Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "Hey, guest",
                  style: txtTheme.bodyLarge?.apply(fontSizeFactor: 1.1),
                ),
                const SizedBox(height: 15),
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
                            final promo =
                                promotionController.promotionData.value[index];
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
                                            child: promotionController.imageUrl
                                                        .value[index] !=
                                                    "none"
                                                ? Image.network(
                                                    promotionController
                                                        .imageUrl.value[index],
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
          }),
        ),
      ),
    );
  }
}
