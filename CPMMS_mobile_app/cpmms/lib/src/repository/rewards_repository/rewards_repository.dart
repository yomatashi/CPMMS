import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:cpmms/src/features/core/models/rewards_model.dart';
import 'package:get/get.dart';
import 'package:firebase_storage/firebase_storage.dart' as firebase_storage;

class RewardsRepository extends GetxController {
  static RewardsRepository get instance => Get.find();

  final _db = FirebaseFirestore.instance;

  Future<List<RewardsModel>> getRewardsList() async {
    final snapshot = await _db.collection("MemberRewards").get();
    final rewardsData =
        snapshot.docs.map((e) => RewardsModel.fromSnapshot(e)).toList();
    return rewardsData;
  }

  Future<RewardsModel> getRewardsDetails(String rewardsID) async {
    final snapshot = await _db
        .collection("MemberRewards")
        .where(FieldPath.documentId, isEqualTo: rewardsID)
        .get();
    final rewardsData =
        snapshot.docs.map((e) => RewardsModel.fromSnapshot(e)).single;
    return rewardsData;
  }

  Future<void> updateRewards(RewardsModel rwrd) async {
    await _db.collection("MemberRewards").doc(rwrd.id).update(rwrd.toJson());
  }

  Future<void> deleteRewards(RewardsModel rwrd) async {
    final storageRef = firebase_storage.FirebaseStorage.instance.ref();
    // Check if the path exists
    final exists = await storageRef
        .child(rwrd.img)
        .getMetadata()
        .then((metadata) => true)
        .catchError((error) => false);

    if (exists) {
      // Delete the file at the specified path
      await storageRef.child(rwrd.img).delete();
    } else {}

    await _db.collection("MemberRewards").doc(rwrd.id).delete().whenComplete(
          () => Get.snackbar("Success", "Successfully deleted!",
              snackPosition: SnackPosition.BOTTOM,
              backgroundColor: Colors.green,
              colorText: Colors.white),
        );
  }

  createRewards(RewardsModel rwrd) async {
    rwrd.id = await _db
        .collection("MemberRewards")
        .add(rwrd.toJson())
        .whenComplete(
          () => Get.snackbar("Success", "New voucher has been added",
              snackPosition: SnackPosition.BOTTOM,
              backgroundColor: Colors.green,
              colorText: Colors.white),
        )
        .then((doc) => doc.id)
        .catchError(
      (error, StackTrace) {
        Get.snackbar("Error", "Something went wrong. Try again",
            snackPosition: SnackPosition.BOTTOM,
            backgroundColor: Colors.redAccent,
            colorText: Colors.white);
      },
    );
    rwrd.img = "rewards/${rwrd.id}.jpg";

    await _db
        .collection("MemberRewards")
        .doc(rwrd.id)
        .update({"img": 'rewards/${rwrd.id}.jpg'});
  }
}