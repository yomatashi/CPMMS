import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/authentications/models/member_model.dart';
import 'package:cpmms/src/features/core/controllers/nav_controller.dart';
import 'package:cpmms/src/features/core/controllers/profile_controller.dart';
import 'package:cpmms/src/features/core/controllers/purchase_controller.dart';
import 'package:cpmms/src/features/core/models/purchase_model.dart';
import 'package:cpmms/src/features/core/screens/profile/profile_screen.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';
import 'package:flutter/material.dart';
import 'package:cpmms/src/features/widget/nav_sidebar/nav_sidebar.dart';
import 'package:get/get.dart';
import 'package:intl/intl.dart';

// class PurchaseHistory extends StatefulWidget {
//   const PurchaseHistory({
//     super.key,
//   });

//   @override
//   _PurchaseHistoryState createState() => _PurchaseHistoryState();
// }

class PurchaseHistory extends StatelessWidget {
  const PurchaseHistory({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    Get.put(NavigationController());
    final controller = Get.put(ProfileController());
    controller.getMemberDataFuture();
    final purchaseController = Get.put(TrackPurchaseController());
    DateFormat dateTimeFormat = DateFormat('dd-MM-yyyy HH:mm');

    var mediaQuery = MediaQuery.of(context);
    double height = mediaQuery.size.height;

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
        title: Text("Consult Pharmacy", style: txtTheme.headlineMedium),
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
              icon: const Icon(Icons.person_2_outlined, color: Colors.black54),
            ),
          ),
        ],
      ),
      drawer: Sidebar(),
      body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.all(tDashboardPadding),
          child: Obx(() {
            MemberModel memberData = controller.memberData.value;
            purchaseController.getPurchaseHistory(memberData.id);
            return Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(
                  height: height * 0.1,
                  child: Row(
                    children: [
                      const Icon(
                        LineAwesomeIcons.history,
                        color: tPrimaryColor,
                      ),
                      const SizedBox(width: 5),
                      Text("Purchase History", style: txtTheme.headlineLarge),
                    ],
                  ),
                ),
                SizedBox(
                  height: height * 0.9,
                  child: ListView.builder(
                    shrinkWrap: true,
                    itemCount:
                        purchaseController.purchaseHistoryData.value.length,
                    itemBuilder: (context, index) {
                      final item =
                          purchaseController.purchaseHistoryData.value[index];
                      String formattedDateTime =
                          dateTimeFormat.format(item.date.toDate());
                      return ExpansionTile(
                        title:
                            Text(formattedDateTime, style: txtTheme.bodyLarge),
                        children: [
                          ListTile(
                            title: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text("Payment Mode: ${item.paymentMode}",
                                    style: txtTheme.bodySmall),
                                const SizedBox(height: 2),
                                Text("Total Price RM: ${item.totalPrice.toStringAsFixed(2)}",
                                    style: txtTheme.bodySmall),
                                const SizedBox(height: 2),
                                Text("List of items:",
                                    style: txtTheme.bodySmall),
                                const SizedBox(height: 2),
                                for (int i = 0; i < item.items.length; i++)
                                  Column(
                                      crossAxisAlignment:
                                          CrossAxisAlignment.start,
                                      children: [
                                        Text(
                                            "Item ${i+1}: ${item.items[i]['itemName']}",
                                            style: txtTheme.bodySmall),
                                        const SizedBox(height: 2),
                                        Text(
                                            "Quantity: ${item.items[i]['qty']}",
                                            style: txtTheme.bodySmall),
                                        const SizedBox(height: 2),
                                        Text(
                                            "Price: RM${item.items[i]['itemPrice'].toStringAsFixed(2)}",
                                            style: txtTheme.bodySmall),
                                        const SizedBox(height: 2),
                                      ]),
                              ],
                            ),
                          )
                        ],
                      );
                    },
                  ),
                ),
              ],
            );
          }),
        ),
      ),
    );
  }
}
