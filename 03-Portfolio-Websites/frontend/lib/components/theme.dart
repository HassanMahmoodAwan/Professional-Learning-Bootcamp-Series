import 'package:flutter/material.dart';

class AppTheme {
  static ThemeData get darkTheme {
    return ThemeData(
      brightness: Brightness.dark,
      scaffoldBackgroundColor: const Color.fromARGB(255, 0, 0, 0),
      primaryColor: Colors.white,
      appBarTheme: const AppBarTheme(
        // backgroundColor: Color.fromARGB(255, 0, 0, 0),
        backgroundColor: Color.fromARGB(255, 35, 35, 35),
        elevation: 0,
      ),
    );
  }
}
