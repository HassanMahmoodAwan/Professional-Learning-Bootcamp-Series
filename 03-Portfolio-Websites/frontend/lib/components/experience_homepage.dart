import 'package:flutter/material.dart';

class ExperienceHomepage extends StatelessWidget {
  const ExperienceHomepage({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        children: [
          Text(
            "Experience",
            style: TextStyle(),
          ),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Present Experience
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                spacing: 4,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text("Senior Software Engineer",
                          style: TextStyle(
                              fontSize: 24, fontWeight: FontWeight.bold)),
                      Text("August-2024 - Present",
                          style: TextStyle(
                              fontSize: 16,
                              fontWeight: FontWeight.bold,
                              fontStyle: FontStyle.italic,
                              color: Colors.grey))
                    ],
                  ),
                  Text("@ Allied Bank Limited",
                      style: TextStyle(
                          fontSize: 15.5, fontWeight: FontWeight.bold)),
                  SizedBox(height: 5),
                  Text(
                    "I am a Senior Software Engineer at Allied Bank Limited (since August 2024), focusing on Generative AI, Machine Learning, and full-stack development. I work with technologies like Python, Flutter, FastAPI, and LangChain to build scalable solutions and AI-powered systems. My role involves driving innovation, automating workflows, and enhancing customer experiences through advanced technology.",
                    style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.bold,
                        color: const Color.fromARGB(255, 180, 180, 180)),
                    textAlign: TextAlign.justify,
                  )
                ],
              ),
            ],
          ),
        ],
      ),
    );
  }
}
