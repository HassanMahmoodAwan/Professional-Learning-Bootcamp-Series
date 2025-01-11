import 'package:flutter/material.dart';
import 'package:frontend/components/custom_appbar.dart';
import 'package:frontend/components/description_homepage.dart';
import 'package:frontend/components/experience_homepage.dart';
import 'package:frontend/components/heading_section.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
          preferredSize: Size.fromHeight(70), child: CustomAppbar()),
      body: Align(
        alignment: Alignment.center,
        child: Container(
          width: MediaQuery.of(context).size.width * 0.60,
          child: ListView(
            children: [
              SizedBox(
                height: 40,
              ),
              Heading(),
              SizedBox(
                height: 60,
              ),
              // Description
              DescriptionHomepage(),

              // Experience
              SizedBox(
                height: 60,
              ),
              ExperienceHomepage()
            ],
          ),
        ),
      ),
    );
  }
}
