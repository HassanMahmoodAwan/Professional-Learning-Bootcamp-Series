import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class DescriptionHomepage extends StatelessWidget {
  const DescriptionHomepage({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: const Color.fromARGB(255, 40, 40, 40),
      child: Align(
        alignment: Alignment.center,
        child: Column(children: [
          SelectableText(
            "I'm a software engineer focused on Full Stack Development and ML/AI. My work combines hands-on engineering with creating technical resources for other developers. I am also working on Generative AI and developing chatbots, exploring innovative applications in conversational AI. Additionally, I am still learning and developing projects to enhance my skills and stay updated with emerging technologies. My interests include understanding the influence of AI on various domains and gaining deeper insights into predictive algorithms in data science.",
            style: TextStyle(
                height: 1.8,
                wordSpacing: 1.8,
                fontSize: 16,
                color: const Color.fromARGB(255, 200, 200, 200)),
            textAlign: TextAlign.justify,
          ),

          // Buttons to Communicate.
          SizedBox(
            height: 30,
          ),
          Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              // GitHub Icon
              ElevatedButton.icon(
                onPressed: () {},
                icon: Icon(
                  Icons.code,
                  color: const Color.fromARGB(255, 115, 85, 205),
                ),
                label: Text(
                  "Github",
                  style: TextStyle(color: Colors.white),
                ),
                style: ElevatedButton.styleFrom(
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8))),
              ),

              SizedBox(
                width: 90,
              ),
              // Linkedin Button
              ElevatedButton.icon(
                onPressed: () {},
                icon: FaIcon(
                  FontAwesomeIcons.linkedin,
                  color: Colors.blueAccent,
                ),
                label: Text(
                  "Linkedin",
                  style: TextStyle(color: Colors.white),
                ),
                style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.blue[900],
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8))),
              )
            ],
          )
        ]),
      ),
    );
  }
}
