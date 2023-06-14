import 'dart:io';

import 'package:cpmms/src/features/authentications/models/member_model.dart';
import 'package:cpmms/src/repository/admin_repository/admin_repository.dart';
import 'package:cpmms/src/repository/authentication_repository/authentication_repository.dart';
import 'package:cpmms/src/repository/member_repository/member_repository.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:firebase_storage/firebase_storage.dart' as firebase_storage;
import 'package:get/get.dart';

class ProfileController extends GetxController {
  static ProfileController get instance => Get.find();

  final _authRepo = Get.put(AuthenticationRepository());
  final _memberRepo = Get.put(MemberRepository());
  final _adminRepo = Get.put(AdminRepository());
  final imageUrl = ''.obs;
  final picker = ImagePicker();

  Rx<MemberModel> memberData = Rx<MemberModel>(
      const MemberModel(id: '',fullName: '', email: '', IC: '', points: 0, pfp: ''));

  getMemberData() {
    final email = _authRepo.firebaseUser.value?.email;
    if (email != null) {
      return _memberRepo.getMemberDetails(email);
    } else {
      Get.snackbar("Error", "Login to continue");
    }
  }

  Future<void> getMemberDataFuture() async {
    final email = _authRepo.firebaseUser.value?.email;
    if (email != null) {
      final data = await _memberRepo.getMemberDetails(email);
      memberData.value = data;
      Get.find<ProfileController>().getPFP(data.pfp);
    } else {
      Get.snackbar("Error", "Login to continue");
    }
  }

  Future<void> getPFP(String imagePath) async {
    try {
      final ref =
          firebase_storage.FirebaseStorage.instance.ref().child(imagePath);
      final url = await ref.getDownloadURL();
      imageUrl.value = url;
    } catch (e) {
      imageUrl.value = "none";
    }
  }

  Future<void> pickAndUploadImage(String memID) async {
    final pickedImage = await picker.pickImage(source: ImageSource.gallery);
    if (pickedImage != null) {
      final file = File(pickedImage.path);
      final customFileName =
          'pfp/${memID}.jpg';
      await uploadImageToFirebase(file, customFileName);
    }
  }

  Future<void> uploadImageToFirebase(File file, String fileName) async {
    try {
      final firebaseStorageRef =
          firebase_storage.FirebaseStorage.instance.ref().child(fileName);
      await firebaseStorageRef.putFile(file);
      Get.snackbar(
        "Success",
        "Profile photo has been updated!",
        snackPosition: SnackPosition.BOTTOM,
        backgroundColor: Colors.green,
        colorText: Colors.white,
      );
    } catch (e) {
      Get.snackbar(
        "Error",
        "Profile photo could not upload",
        snackPosition: SnackPosition.BOTTOM,
        backgroundColor: Colors.red,
        colorText: Colors.white,
      );
    }
  }

  updateMember(MemberModel member) async {
    await _memberRepo.updateMember(member);
    Get.find<ProfileController>().getMemberDataFuture();
    Get.snackbar(
      "Success",
      "Profile details has been updated!",
      snackPosition: SnackPosition.BOTTOM,
      backgroundColor: Colors.green,
      colorText: Colors.white,
    );
  }

  getAdminData() {
    final email = _authRepo.firebaseUser.value?.email;
    if (email != null) {
      return _adminRepo.getAdminDetails(email);
    } else {
      Get.snackbar("Error", "Login to continue");
    }
  }
}
