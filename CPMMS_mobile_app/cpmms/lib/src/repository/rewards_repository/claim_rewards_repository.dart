import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:cpmms/src/features/core/models/claim_rewards_model.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class ClaimRewardsRepository extends GetxController {
  static ClaimRewardsRepository get instance => Get.find();

  final _db = FirebaseFirestore.instance;

  Future<List<ClaimRewardsModel>> getClaimRewardsList(String memberID) async {
    final snapshot = await _db
        .collection("ClaimRewards")
        .where("memberID", isEqualTo: memberID)
        .get();
    final ClaimRewardsData =
        snapshot.docs.map((e) => ClaimRewardsModel.fromSnapshot(e)).toList();
    return ClaimRewardsData;
  }

  Future<ClaimRewardsModel> getClaimRewardsDetails(String claimRewardID) async {
    final snapshot = await _db
        .collection("ClaimRewards")
        .where(FieldPath.documentId, isEqualTo: claimRewardID)
        .get();
    final ClaimRewardData =
        snapshot.docs.map((e) => ClaimRewardsModel.fromSnapshot(e)).single;
    return ClaimRewardData;
  }

  createClaimReward(ClaimRewardsModel claimReward) async {
    await _db
        .collection("ClaimRewards")
        .add(claimReward.toJson())
        .whenComplete(
          () => Get.snackbar("Success",
              "Voucher has been claimed! Please check the 'My Voucher' tab.",
              snackPosition: SnackPosition.BOTTOM,
              backgroundColor: Colors.green,
              colorText: Colors.white),
        )
        .catchError(
      (error, StackTrace) {
        Get.snackbar("Error", "Something went wrong. Try again",
            snackPosition: SnackPosition.BOTTOM,
            backgroundColor: Colors.redAccent,
            colorText: Colors.white);
      },
    );
  }

  Future<void> updateClaimReward(ClaimRewardsModel claimRwrd) async {
    await _db
        .collection("ClaimRewards")
        .doc(claimRwrd.id)
        .update(claimRwrd.toJson());
  }

  Future<void> deleteClaimReward(String rewardID) async {
    //   await _db.collection("ClaimRewards").where("rewardsID", isEqualTo: rewardID).delete().whenComplete(
    //         () => Get.snackbar("Success", "Successfully deleted!",
    //             snackPosition: SnackPosition.BOTTOM,
    //             backgroundColor: Colors.green,
    //             colorText: Colors.white),
    //       );
    QuerySnapshot querySnapshot = await _db
        .collection("ClaimRewards")
        .where("rewardsID", isEqualTo: rewardID)
        .get();
    List<Future<void>> deleteFutures = [];
    querySnapshot.docs.forEach((doc) {
      deleteFutures.add(doc.reference.delete());
    });
    await Future.wait(deleteFutures);
  }
}
