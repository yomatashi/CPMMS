import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:cpmms/src/features/authentications/screens/welcome/welcome_screen.dart';
import 'package:cpmms/src/features/core/screens/dashboard/dashboard.dart';
import 'package:cpmms/src/features/core/screens/dashboard/dashboard_admin.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class AuthenticationRepository extends GetxController {
  static AuthenticationRepository get instance => Get.find();

  //  variables
  final _auth = FirebaseAuth.instance;
  late final Rx<User?> firebaseUser;
  String errMsg = "An unknown error occured.";

  @override
  void onReady() {
    // Future.delayed(const Duration(seconds: 6));
    firebaseUser = Rx<User?>(_auth.currentUser);
    firebaseUser.bindStream(_auth.userChanges());
    ever(firebaseUser, _setInitialScreen);
  }

  Future<void> _setInitialScreen(User? user) async {
    if (user == null) {
      Get.offAll(() => const WelcomeScreen());
    } else {
      QuerySnapshot snapshot = await FirebaseFirestore.instance
          .collection("Member")
          .where('email', isEqualTo: firebaseUser.value?.email)
          .get();
      snapshot.docs.isNotEmpty
          ? Get.offAll(() => const Dashboard())
          : Get.offAll(() => const DashboardAdmin());
    }
  }

  Future<void> loginWithEmailAndPassword(String email, String password) async {
    try {
      await _auth.signInWithEmailAndPassword(email: email, password: password);
      if (firebaseUser.value != null) {
        QuerySnapshot snapshot = await FirebaseFirestore.instance
            .collection("Member")
            .where('email', isEqualTo: email)
            .get();
        snapshot.docs.isNotEmpty
            ? Get.offAll(() => const Dashboard())
            : Get.offAll(() => const DashboardAdmin());
      } else {
        Get.to(() => const WelcomeScreen());
      }
    } on FirebaseAuthException catch (e) {
      switch (e.code) {
        case 'user-not-found':
          errMsg = "User not found!";
          break;
        case 'wrong-password':
          errMsg = "Wrong password!";
          break;
        case 'network-request-failed':
          errMsg = "Network failed! Please connect to the internet.";
          break;
        case 'invalid-email':
          errMsg = "Email address is badly formatted.";
          break;
      }
      Get.snackbar("Error", errMsg,
          snackPosition: SnackPosition.BOTTOM,
          backgroundColor: Colors.red.withOpacity(0.1),
          colorText: Colors.red);
    } catch (e) {
      e.printError();
    }
  }

  Future<void> logout() async => await _auth.signOut();
}
