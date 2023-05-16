import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/authentications/screens/login/login_screen.dart';
import 'package:cpmms/src/features/core/screens/dashboard/dashboard_guest.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var mediaQuery = MediaQuery.of(context);
    double height = mediaQuery.size.height;
    return Scaffold(
      backgroundColor: tPrimaryColor,
      body: Container(
        padding: const EdgeInsets.all(tDefaultSize),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Image(
                image: const AssetImage(tWelcomeScreenImage),
                height: height * 0.6),
            Column(
              children: [
                Text(
                  "Welcome",
                  style: Theme.of(context).textTheme.headlineLarge,
                ),
                Text(
                  "Let's get started",
                  style: Theme.of(context).textTheme.bodyLarge,
                  textAlign: TextAlign.center,
                ),
              ],
            ),
            Row(
              children: [
                Expanded(
                  child: ElevatedButton(
                    onPressed: () => Get.to(() => const LoginScreen()),
                    style: ElevatedButton.styleFrom(
                      elevation: 0,
                      shape: const RoundedRectangleBorder(),
                      foregroundColor: tWhiteColor,
                      backgroundColor: tSecondaryColor,
                      side: const BorderSide(color: tSecondaryColor),
                      padding:
                          const EdgeInsets.symmetric(vertical: tButtonHeight),
                    ),
                    child: Text("Login".toUpperCase()),
                  ),
                ),
              ],
            ),
            Row(
              children: [
                Expanded(
                  child: OutlinedButton(
                    onPressed: () {Get.to(const DashboardGuest());},
                    style: OutlinedButton.styleFrom(
                      shape: const RoundedRectangleBorder(),
                      foregroundColor: tSecondaryColor,
                      side: const BorderSide(color: tSecondaryColor),
                      padding:
                          const EdgeInsets.symmetric(vertical: tButtonHeight),
                    ),
                    child: Text("Login as Guest".toUpperCase()),
                  ),
                )
              ],
            ),
          ],
        ),
      ),
    );
  }
}
