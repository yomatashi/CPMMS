import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/authentications/models/admin_model.dart';
import 'package:cpmms/src/features/authentications/models/member_model.dart';
import 'package:cpmms/src/features/core/controllers/promotion_controller.dart';
import 'package:cpmms/src/features/core/screens/member_points/member_points.dart';
import 'package:cpmms/src/features/core/screens/profile/update_profile_screen.dart';
import 'package:cpmms/src/features/core/screens/promotion/promotion_admin.dart';
import 'package:cpmms/src/features/core/screens/purchase_history/purchase_history.dart';
import 'package:cpmms/src/features/core/screens/rewards/rewards_admin.dart';
import 'package:cpmms/src/repository/authentication_repository/authentication_repository.dart';
import 'package:cpmms/src/features/core/controllers/profile_controller.dart';
import 'package:flutter/material.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';
import 'package:get/get.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({required this.role, Key? key}) : super(key: key);

  final String role;
  @override
  Widget build(BuildContext context) {
    final controller = Get.put(ProfileController());
    role == "Member"
        ? controller.getMemberDataFuture()
        : controller.getAdminDataFuture();
    final promoController = Get.put(PromotionController());
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            Get.back();
          },
          icon: const Icon(LineAwesomeIcons.angle_left, color: Colors.black54),
        ),
        title: Text(
          "Profile",
          style: Theme.of(context).textTheme.headlineMedium,
        ),
        centerTitle: true,
        elevation: 0,
        backgroundColor: Colors.transparent,
      ),
      body: SingleChildScrollView(
        child: Container(
            padding: const EdgeInsets.all(tDefaultSize),
            child: Obx(() {
              if (role == "Member") {
                MemberModel memberData = controller.memberData.value;
                var fullName = memberData.fullName;
                var email = memberData.email;
                return Column(
                  children: [
                    Stack(children: [
                      SizedBox(
                        width: 120,
                        height: 120,
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(100),
                          child: controller.imageUrl.value != "none"
                              ? Image.network(controller.imageUrl.value)
                              : Image.asset(tDefaultPfp),
                        ),
                      ),
                    ]),
                    const SizedBox(height: 10),
                    Text(fullName,
                        style: Theme.of(context).textTheme.headlineMedium),
                    Text(email, style: Theme.of(context).textTheme.bodyLarge),
                    const SizedBox(height: 20),
                    SizedBox(
                      width: 200,
                      child: ElevatedButton(
                        onPressed: () =>
                            Get.to(() => const UpdateProfileScreen()),
                        style: ElevatedButton.styleFrom(
                            backgroundColor: tPrimaryColor,
                            side: BorderSide.none,
                            shape: const StadiumBorder()),
                        child: const Text(
                          "Edit Profile",
                          style: TextStyle(color: tDarkColor),
                        ),
                      ),
                    ),
                    const SizedBox(height: 30),
                    const Divider(),
                    const SizedBox(height: 10),

                    // MENU
                    ProfileMenuWidget(
                      title: "Purchase History",
                      icon: LineAwesomeIcons.history,
                      onPress: () {
                        Get.off(const PurchaseHistory());
                      },
                    ),
                    ProfileMenuWidget(
                      title: "Check member points",
                      icon: LineAwesomeIcons.identification_card,
                      onPress: () {
                        Get.off(const MemberPoints());
                      },
                    ),
                    const Divider(color: Colors.grey),
                    const SizedBox(height: 30),
                    ProfileMenuWidget(
                      title: "Logout",
                      icon: LineAwesomeIcons.alternate_sign_out,
                      textColor: Colors.red,
                      endIcon: false,
                      onPress: () {
                        AuthenticationRepository.instance.logout();
                      },
                    ),
                  ],
                );
              } else {
                AdminModel adminData = controller.adminData.value;
                var fullName = adminData.fullName;
                var email = adminData.email;
                return Column(
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
                    ]),
                    const SizedBox(height: 10),
                    Text(fullName,
                        style: Theme.of(context).textTheme.headlineMedium),
                    Text(email, style: Theme.of(context).textTheme.bodyLarge),
                    const SizedBox(height: 20),
                    SizedBox(
                      width: 200,
                      child: ElevatedButton(
                        onPressed: () => Get.snackbar("Information",
                            "Please update your user information in CPMMS desktop app.", colorText: Colors.white, backgroundColor: Colors.blue, icon: const Icon(LineAwesomeIcons.info)),
                        style: ElevatedButton.styleFrom(
                            backgroundColor: tPrimaryColor,
                            side: BorderSide.none,
                            shape: const StadiumBorder()),
                        child: const Text(
                          "Edit Profile",
                          style: TextStyle(color: tDarkColor),
                        ),
                      ),
                    ),
                    const SizedBox(height: 30),
                    const Divider(),
                    const SizedBox(height: 10),

                    // MENU
                    ProfileMenuWidget(
                      title: "Edit member rewards",
                      icon: LineAwesomeIcons.gift,
                      onPress: () {
                        Get.off(const RewardsManager());
                      },
                    ),
                    ProfileMenuWidget(
                      title: "Edit promotion",
                      icon: LineAwesomeIcons.tags,
                      onPress: () {
                        promoController.isLoading.value = true;
                        Get.off(const PromotionManager());
                      },
                    ),
                    const Divider(color: Colors.grey),
                    const SizedBox(height: 30),
                    ProfileMenuWidget(
                      title: "Logout",
                      icon: LineAwesomeIcons.alternate_sign_out,
                      textColor: Colors.red,
                      endIcon: false,
                      onPress: () {
                        AuthenticationRepository.instance.logout();
                      },
                    ),
                  ],
                );
              }
            })),
      ),
    );
  }
}

class ProfileMenuWidget extends StatelessWidget {
  const ProfileMenuWidget({
    Key? key,
    required this.title,
    required this.icon,
    required this.onPress,
    this.endIcon = true,
    this.textColor,
  }) : super(key: key);

  final String title;
  final IconData icon;
  final VoidCallback onPress;
  final bool endIcon;
  final Color? textColor;

  @override
  Widget build(BuildContext context) {
    var isDark = MediaQuery.of(context).platformBrightness == Brightness.dark;
    var iconColor = isDark ? tPrimaryColor : tAccentColor;
    return ListTile(
      onTap: onPress,
      leading: Container(
        width: 40,
        height: 40,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(100),
          color: iconColor.withOpacity(0.1),
        ),
        child: Icon(icon, color: iconColor),
      ),
      title: Text(title,
          style:
              Theme.of(context).textTheme.bodySmall?.apply(color: textColor)),
      trailing: endIcon
          ? Container(
              width: 30,
              height: 30,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(100),
                color: Colors.grey.withOpacity(0.1),
              ),
              child: const Icon(
                LineAwesomeIcons.angle_right,
                size: 18.0,
                color: Colors.grey,
              ),
            )
          : null,
    );
  }
}
