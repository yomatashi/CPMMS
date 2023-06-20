import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/authentications/models/member_model.dart';
import 'package:cpmms/src/features/core/controllers/pts_controller.dart';
import 'package:cpmms/src/features/core/controllers/nav_controller.dart';
import 'package:cpmms/src/features/core/controllers/profile_controller.dart';
import 'package:cpmms/src/features/core/screens/profile/profile_screen.dart';
import 'package:flutter/material.dart';
import 'package:cpmms/src/features/widget/nav_sidebar/nav_sidebar.dart';
import 'package:get/get.dart';
import 'package:intl/intl.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';

class MemberPoints extends StatelessWidget {
  const MemberPoints({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    Get.put(NavigationController());
    final controller = Get.put(ProfileController());
    controller.getMemberDataFuture();
    final ptsHistoryController = Get.put(PointsHistoryController());
    var mediaQuery = MediaQuery.of(context);
    double height = mediaQuery.size.height;
    double width = mediaQuery.size.width;
    DateFormat dateTimeFormat = DateFormat('dd-MM-yyyy HH:mm');

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
            if (controller.memberData.value != null) {
              MemberModel memberData = controller.memberData.value;
              int pts = memberData.points;
              ptsHistoryController.getPtsHistory(memberData.id);
              final formattedNumber = NumberFormat('#,###').format(pts);
              return Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    color: tPrimaryColor,
                    height: height * 0.3,
                    child: Center(
                      child: Text(
                        "TOTAL POINTS: $formattedNumber",
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 20),
                  Row(
                    children: [
                      const Icon(
                        LineAwesomeIcons.history,
                        color: tPrimaryColor,
                      ),
                      const SizedBox(width: 5),
                      Text("Points History", style: txtTheme.headlineSmall),
                    ],
                  ),
                  SizedBox(
                    height: height * 0.5,
                    child: ListView.builder(
                      shrinkWrap: true,
                      itemCount:
                          ptsHistoryController.ptsHistoryData.value.length,
                      itemBuilder: (context, index) {
                        final item =
                            ptsHistoryController.ptsHistoryData.value[index];
                        String formattedDateTime = dateTimeFormat.format(item.date.toDate());
                        return ListTile(
                          contentPadding: const EdgeInsets.all(0),
                          title: FittedBox(
                            fit: BoxFit.scaleDown,
                            child: Row(children: [
                              SizedBox(
                                width: width * 0.7,
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(item.name, style: txtTheme.bodyLarge),
                                    Text(formattedDateTime, style: txtTheme.bodySmall),
                                  ],
                                ),
                              ),
                              SizedBox(
                                width: width * 0.3,
                                child: Center(
                                  child: Text(
                                    item.pointsDiff.toString(),
                                    style: txtTheme.headlineSmall?.apply(color: item.pointsDiff<0 ? Colors.red : Colors.green),
                                  ),
                                ),
                              ),
                            ]),
                          ),
                        );
                      },
                    ),
                  ),
                ],
              );
            } else {
              return const Center(child: CircularProgressIndicator());
            }
          }),
        ),
      ),
    );
  }
}
