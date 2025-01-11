import 'package:flutter/material.dart';

class Heading extends StatelessWidget {
  const Heading({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text("Hey, I'm ",
                style: TextStyle(
                    fontSize: 52,
                    fontWeight: FontWeight.bold,
                    color: const Color.fromARGB(255, 152, 152, 152))),
            Text("Hassan Mahmood",
                style: TextStyle(fontSize: 44, fontWeight: FontWeight.bold)),
          ],
        ),
        SizedBox(
          height: 10,
        ),
        Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text("Software Engineer ",
                style: TextStyle(
                    fontSize: 19,
                    fontWeight: FontWeight.bold,
                    color: const Color.fromARGB(255, 156, 156, 156))),
            Text(" and ",
                style: TextStyle(
                    fontSize: 19,
                    color: const Color.fromARGB(255, 98, 98, 98))),
            Text("Generative AI enthusiast",
                style: TextStyle(
                    fontSize: 19,
                    fontWeight: FontWeight.bold,
                    color: const Color.fromARGB(255, 156, 156, 156))),
          ],
        )
      ],
    );
  }
}
