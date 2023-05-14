import 'package:cpmms/src/constants/sizes.dart';
import 'package:flutter/material.dart';

class ForgetPasswordMailScreen extends StatelessWidget {
  const ForgetPasswordMailScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: SingleChildScrollView(
          child: Container(
            padding: const EdgeInsets.all(tDefaultSize),
            child: Column(
              children: const [
                SizedBox(height: tDefaultSize * 4),
                ForgotPwForm(),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class ForgotPwForm extends StatelessWidget {
  const ForgotPwForm({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Form(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: tFormHeight - 10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text("Forget Password", style: Theme.of(context).textTheme.headlineLarge),
            const SizedBox(height: tFormHeight - 10),
            Text("Enter the email associated with your account and we'll send an email with instructions to reset your password.", style: Theme.of(context).textTheme.bodySmall),
            const SizedBox(height: tFormHeight - 10),
            TextFormField(
              decoration: const InputDecoration(
                prefixIcon: Icon(Icons.person_outline_outlined),
                labelText: "E-Mail",
                hintText: "example@gmail.com",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: tFormHeight - 20),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () {},
                child: const Text("Send Email"),
              ),
            ),
            const SizedBox(height: tFormHeight - 20),
          ],
        ),
      ),
    );
  }
}
