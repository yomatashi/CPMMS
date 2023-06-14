import 'package:cpmms/src/constants/colors.dart';
import 'package:flutter/material.dart';

class CircularButton extends StatelessWidget {
  const CircularButton({required this.icon, required this.text, required this.onPressed, Key? key})
      : super(key: key);

  final IconData icon;
  final String text;
  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onPressed,
      child: Container(
        margin: const EdgeInsets.all(8), // Set the desired margin
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            CircleAvatar(
              radius: 38,
              backgroundColor: tPrimaryColor, // Set the desired circle color
              child: Flex(
                direction: Axis.vertical,
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Icon(icon),
                  const SizedBox(height: 4),
                  Flexible(
                    child: Text(
                      text,
                      textAlign: TextAlign.center,
                      style: const TextStyle(fontSize: 12, color: Colors.white), // Set the desired text size and color
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
