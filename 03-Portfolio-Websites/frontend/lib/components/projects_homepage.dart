import 'package:flutter/material.dart';

class ProjectsHomepage extends StatelessWidget {
  const ProjectsHomepage({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        children: [
          Text(
            "PROJECTS",
            style: TextStyle(
                fontSize: 24, color: Colors.white, fontWeight: FontWeight.bold),
          )
        ],
      ),
    );
  }
}
