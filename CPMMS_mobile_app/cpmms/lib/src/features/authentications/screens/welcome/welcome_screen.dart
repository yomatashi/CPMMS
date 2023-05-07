import 'package:cpmms/src/constants/image_strings.dart';
import 'package:flutter/material.dart';

class WelcomeScreen extends StatelessWidget{
  const WelcomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context){
    return Scaffold(
      body: Container(
        child: Column(
          children: [
            const Image(image :AssetImage(tWelcomeScreenImage)),
            const Text("Build Awesome Apps"),
            const Text("wau"),
            Row(
              children: [
                OutlinedButton(onPressed: (){}, child: const Text("Login")),
                ElevatedButton(onPressed: (){}, child: const Text("Signup")),
              ],
            )
          ],
        ),
      ),
    );
  }
}