import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:flutter/material.dart';

class SignupScreen extends StatelessWidget {
  const SignupScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    return SafeArea(
      child: Scaffold(
          body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.all(tDefaultSize),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Image(
                  image: const AssetImage(tLogoImage),
                  height: size.height * 0.2),
              Align(
                alignment: Alignment.center,
                child: Text(
                    "Join Us!",
                    style: Theme.of(context).textTheme.headlineLarge,
                  ),
              ),
              const SizedBox(height: tFormHeight - 10),
              Text(
                  "Register as a our member now and enjoy the benefits of our membership program. Please visit our nearest store and our staff will be happy to assist you with the registration process. As a member, you will receive exclusing discounts, promotions and other perks. Don't miss out on these great benefits, register now at our nearest store!",
                  style: Theme.of(context).textTheme.bodyLarge,
                  textAlign: TextAlign.justify,
                  
                ),
            ],
          ),
        ),
      )),
    );
  }
}