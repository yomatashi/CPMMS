import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:flutter/material.dart';

class SplashScreen extends StatelessWidget {
  const SplashScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: tPrimaryColor,
      body: Center(
        child: Image.asset(
          tLogoImage, // Replace with your image asset path
          width: 200,
          height: 200,
        ),
      ),
    );
  }
}
