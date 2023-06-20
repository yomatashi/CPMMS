import 'dart:io';
import 'package:cpmms/src/features/core/models/claim_rewards_model.dart';
import 'package:cpmms/src/features/core/models/rewards_model.dart';
import 'package:cpmms/src/features/core/screens/rewards/rewards.dart';
import 'package:cpmms/src/features/core/screens/rewards/rewards_admin.dart';
import 'package:cpmms/src/repository/rewards_repository/claim_rewards_repository.dart';
import 'package:cpmms/src/repository/rewards_repository/rewards_repository.dart';
import 'package:get/get.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:firebase_storage/firebase_storage.dart' as firebase_storage;

class RewardsController extends GetxController {
  static RewardsController get instance => Get.find();

  final _rewardsRepo = Get.put(RewardsRepository());
  final _claimRewardsRepo = Get.put(ClaimRewardsRepository());
  final RxBool isLoading = true.obs;
  final RxBool isLoading2 = true.obs;
  final RxList<String> imageUrl = <String>[].obs;
  final singleImageUrl = ''.obs;
  final RxList<String> imgURLforClaimRwrd = <String>[].obs;
  final picker = ImagePicker();
  Rx<File?> imageFile = Rx<File?>(null);

  RxList<RewardsModel> rewardsData = RxList<RewardsModel>();
  RxList<ClaimRewardsModel> claimRewardsData = RxList<ClaimRewardsModel>();
  RxList<RewardsModel> claimRewardsDetails = RxList<RewardsModel>();

  // Textfield controllers
  final rewardsTitle = TextEditingController();
  final rewardsInstruction = TextEditingController();
  final rewardsCost = TextEditingController();

  Future<void> getRewardsList() async {
    final data = await _rewardsRepo.getRewardsList();
    rewardsData.value = data;
    Get.find<RewardsController>().getImg();
  }

  Future<void> getImg() async {
    imageUrl.value =
        List<String>.filled(rewardsData.length, "", growable: true).obs;

    for (var i = 0; i < rewardsData.length; i++) {
      final promoData = rewardsData[i];
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

  getRewardsData(String rewardsID) async {
    final data = await _rewardsRepo.getRewardsDetails(rewardsID);
    Get.find<RewardsController>().getSingleImg(data.img);
    return data;
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

  Future<void> getClaimRewardsList(String memID) async {
    // get all claim rewards by user
    final data = await _claimRewardsRepo.getClaimRewardsList(memID);
    claimRewardsData.value = data;
    // get the claim rewards information/details
    for (int i = 0; i < claimRewardsData.value.length; i++) {
      final rewardsData = await _rewardsRepo
          .getRewardsDetails(claimRewardsData.value[i].rewardsID);
      claimRewardsDetails.add(rewardsData);

      try {
        final ref = firebase_storage.FirebaseStorage.instance
            .ref()
            .child(claimRewardsDetails[i].img);
        final url = await ref.getDownloadURL();
        imgURLforClaimRwrd.add(url);
      } catch (e) {
        imgURLforClaimRwrd.add("none");
      }
    }
    isLoading2.value = false;
  }

  Future<void> createClaimRewards(ClaimRewardsModel claimRewards) async {
    await _claimRewardsRepo.createClaimReward(claimRewards);
    isLoading.value = true;
    isLoading2.value = true;
    Get.off(() => const Rewards());
  }

  getClaimRewardData(String claimRewardID) async {
    final data = await _claimRewardsRepo.getClaimRewardsDetails(claimRewardID);
    return data;
  }

  updateClaimReward(ClaimRewardsModel claimRwrd) async {
    await _claimRewardsRepo.updateClaimReward(claimRwrd);
    Get.snackbar(
      "Success",
      "Voucher has been successfully claimed!",
      snackPosition: SnackPosition.BOTTOM,
      backgroundColor: Colors.green,
      colorText: Colors.white,
    );
    isLoading.value = true;
    isLoading2.value = true;
    Get.off(() => const Rewards());
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

  updateRewards(RewardsModel rwrd) async {
    await _rewardsRepo.updateRewards(rwrd);
    await uploadImageToFirebase(rwrd.img);
    Get.snackbar(
      "Success",
      "Voucher details has been updated!",
      snackPosition: SnackPosition.BOTTOM,
      backgroundColor: Colors.green,
      colorText: Colors.white,
    );
    isLoading.value = true;
    isLoading2.value = true;
    Get.off(() => const RewardsManager());
  }

  Future<void> uploadImageToFirebase(String fileName) async {
    File? file = imageFile.value;
    if (file != null) {
      try {
        final firebaseStorageRef =
            firebase_storage.FirebaseStorage.instance.ref().child(fileName);
        await firebaseStorageRef.putFile(file);
      } catch (e) {
        Get.snackbar("Error", "Voucher image could not upload",
            snackPosition: SnackPosition.BOTTOM,
            backgroundColor: Colors.redAccent,
            colorText: Colors.white);
      }
    }
  }

  Future<void> deleteRewards(RewardsModel rwrd) async{
    await _rewardsRepo.deleteRewards(rwrd);
    await _claimRewardsRepo.deleteClaimReward(rwrd.id);
    isLoading.value = true;
    isLoading2.value = true;
    Get.off(() => const RewardsManager());
  }

Future<void> createReward(RewardsModel rwrd) async {
    await _rewardsRepo.createRewards(rwrd);
    await uploadImageToFirebase(rwrd.img);
    isLoading.value = true;
    isLoading2.value = true;
    Get.off(() => const RewardsManager());
  }
}
