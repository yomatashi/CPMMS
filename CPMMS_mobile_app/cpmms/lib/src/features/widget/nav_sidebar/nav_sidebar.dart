import 'package:cpmms/src/constants/colors.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:cpmms/src/features/core/controllers/nav_controller.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';

class Sidebar extends StatelessWidget {
  Sidebar({Key? key}) : super(key: key);
  final NavigationController navigationController = Get.find();

  void navigateToPage(int index) {
    navigationController.changePage(index);
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
          ListTile(
            leading: const Icon(LineAwesomeIcons.identification_card,
                color: tPrimaryColor),
            title: Text('Member Points', style: txtTheme.headlineSmall),
            onTap: () => navigateToPage(1),
          ),
          ListTile(
            leading: const Icon(LineAwesomeIcons.gift, color: tPrimaryColor),
            title: Text('Rewards', style: txtTheme.headlineSmall),
            onTap: () => navigateToPage(2),
          ),
          ListTile(
            leading:
                const Icon(LineAwesomeIcons.history, color: tPrimaryColor),
            title: Text('Purchase History', style: txtTheme.headlineSmall),
            onTap: () => navigateToPage(3),
          ),
          // ListTile(
          //   leading: const Icon(LineAwesomeIcons.credit_card,
          //       color: tPrimaryColor),
          //   title: Text('Online Payment', style: txtTheme.headlineSmall),
          //   onTap: () => navigateToPage(4),
          // ),
        ],
      ),
    );
  }
}
