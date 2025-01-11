import 'package:flutter/material.dart';

class CustomAppbar extends StatelessWidget {
  const CustomAppbar({super.key});

  @override
  Widget build(BuildContext context) {
    return AppBar(

        // Title Should have Logo
        title: Padding(
      padding: const EdgeInsets.symmetric(horizontal: 15),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Row(
            children: [
              Text("Hassan",
                  style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold)),
              Text("Mahmood",
                  style: TextStyle(
                      fontSize: 14,
                      fontWeight: FontWeight.bold,
                      color: const Color.fromARGB(255, 139, 139, 139)))
            ],
          ),

          // Icons
          Text("Icons",
              style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold)),
        ],
      ),
    ));
  }
}
