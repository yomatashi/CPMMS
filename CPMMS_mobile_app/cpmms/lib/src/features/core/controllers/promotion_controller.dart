import 'dart:io';
import 'package:cpmms/src/features/authentications/models/promotion_model.dart';
import 'package:cpmms/src/features/core/screens/promotion/promotion_admin.dart';
import 'package:cpmms/src/repository/promotion_repository/promotion_repository.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:firebase_storage/firebase_storage.dart' as firebase_storage;
import 'package:get/get.dart';

class PromotionController extends GetxController {
  static PromotionController get instance => Get.find();

  final _promoRepo = Get.put(PromotionRepository());
  final RxList<String> imageUrl = <String>[].obs;
  final RxBool isLoading = true.obs;
  final picker = ImagePicker();
  Rx<File?> imageFile = Rx<File?>(null);
  final singleImageUrl = ''.obs;

  // Textfield controllers
  final promoName = TextEditingController();
  final promoDetails = TextEditingController();

  RxList<PromotionModel> promotionData = RxList<PromotionModel>();

  Future<void> getPromotionList() async {
    final data = await _promoRepo.getPromotionList();
    promotionData.value = data;
    Get.find<PromotionController>().getImg();
  }

  Future<void> getImg() async {
    imageUrl.value =
        List<String>.filled(promotionData.length, "", growable: true).obs;

    for (var i = 0; i < promotionData.length; i++) {
      final promoData = promotionData[i];
      try {
        final ref = firebase_storage.FirebaseStorage.instance
            .ref()
            .child(promoData.img);
        final url = await ref.getDownloadURL();
        imageUrl.value[i] = url;
      } catch (e) {
        imageUrl.value[i] = "none";
      }
    }
    isLoading.value = false;
  }

  getPromoData(String promoID) async {
    final data = await _promoRepo.getPromotionDetails(promoID);
    Get.find<PromotionController>().getSingleImg(data.img);
    return data;
  }

  updatePromo(PromotionModel promo) async {
    await _promoRepo.updatePromotion(promo);
    await uploadImageToFirebase(promo.img);
    Get.snackbar(
      "Success",
      "Promotion details has been updated!",
      snackPosition: SnackPosition.BOTTOM,
      backgroundColor: Colors.green,
      colorText: Colors.white,
    );
    isLoading.value = true;
    Get.off(() => const PromotionManager());
  }

  Future<void> getSingleImg(String imagePath) async {
    try {
      final ref =
          firebase_storage.FirebaseStorage.instance.ref().child(imagePath);
      final url = await ref.getDownloadURL();
      singleImageUrl.value = url;
    } catch (e) {
      singleImageUrl.value = "none";
    }
  }

  Future<void> pickImage() async {
    final pickedImage = await picker.pickImage(source: ImageSource.gallery);
    if (pickedImage != null) {
      final file = File(pickedImage.path);
      imageFile.value = file;
      Get.snackbar(
        "Success",
        "Image uploaded!",
        snackPosition: SnackPosition.BOTTOM,
        backgroundColor: Colors.green,
        colorText: Colors.white,
      );
    }
  }

  Future<void> uploadImageToFirebase(String fileName) async {
    File? file = imageFile.value;
    if (file != null) {
      try {
        final firebaseStorageRef =
            firebase_storage.FirebaseStorage.instance.ref().child(fileName);
        await firebaseStorageRef.putFile(file);
      } catch (e) {
        Get.snackbar("Error", "Promotion image could not upload",
            snackPosition: SnackPosition.BOTTOM,
            backgroundColor: Colors.redAccent,
            colorText: Colors.white);
      }
    }
  }

  Future<void> createPromotion(PromotionModel promo) async {
    await _promoRepo.createPromotion(promo);
    await uploadImageToFirebase(promo.img);
    isLoading.value = true;
    Get.off(() => const PromotionManager());
  }

  Future<void> deletePromotion(PromotionModel promo) async{
    await _promoRepo.deletePromotion(promo);
    isLoading.value = true;
    Get.off(() => const PromotionManager());
  }
}
