import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:cpmms/src/constants/colors.dart';

class TTextTheme{
  TTextTheme._();

  static TextTheme lightTextTheme = TextTheme(
    headlineLarge: GoogleFonts.montserrat(fontSize: 28.0, fontWeight: FontWeight.bold, color: tDarkColor),
    headlineMedium: GoogleFonts.montserrat(fontSize: 24.0, fontWeight: FontWeight.w700, color: tDarkColor),
    headlineSmall: GoogleFonts.poppins(fontSize: 24.0, fontWeight: FontWeight.w600, color: tDarkColor),
    bodyLarge: GoogleFonts.poppins(fontSize: 16.0, fontWeight: FontWeight.normal, color: tDarkColor),
    bodyMedium: GoogleFonts.poppins(fontSize: 14.0, fontWeight: FontWeight.normal, color: tDarkColor),
    bodySmall: GoogleFonts.poppins(fontSize: 14.0, fontWeight: FontWeight.normal, color: tDarkColor),
  );

  static TextTheme darkTextTheme= TextTheme(
    headlineLarge: GoogleFonts.montserrat(fontSize: 28.0, fontWeight: FontWeight.bold, color: tWhiteColor),
    headlineMedium: GoogleFonts.montserrat(fontSize: 24.0, fontWeight: FontWeight.w700, color: tWhiteColor),
    headlineSmall: GoogleFonts.poppins(fontSize: 24.0, fontWeight: FontWeight.w600, color: tWhiteColor),
    bodyLarge: GoogleFonts.poppins(fontSize: 16.0, fontWeight: FontWeight.normal, color: tWhiteColor),
    bodyMedium: GoogleFonts.poppins(fontSize: 14.0, fontWeight: FontWeight.normal, color: tWhiteColor),
    bodySmall: GoogleFonts.poppins(fontSize: 14.0, fontWeight: FontWeight.normal, color: tWhiteColor),
  );
}