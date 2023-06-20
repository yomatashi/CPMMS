import 'package:cpmms/src/constants/colors.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:cpmms/src/features/core/controllers/nav_controller.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';

class SidebarGuest extends StatelessWidget {
  SidebarGuest({Key? key}) : super(key: key);
  final NavigationController navigationController = Get.find();

  void navigateToPage(int index) {
    navigationController.changePageGuest(index);
    Get.back();
  }

  @override
  Widget build(BuildContext context) {
    final txtTheme = Theme.of(context).textTheme;
    return Drawer(
      child: ListView(
        children: [
          const SizedBox(height: 20),
          ListTile(
            leading: const Icon(LineAwesomeIcons.home, color: tPrimaryColor),
            title: Text('Home', style: txtTheme.headlineSmall),
            onTap: () => navigateToPage(0),
          ),
        ],
      ),
    );
  }
}
