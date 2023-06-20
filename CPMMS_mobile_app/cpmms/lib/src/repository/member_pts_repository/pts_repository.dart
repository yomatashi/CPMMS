import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:cpmms/src/features/core/models/pts_history_model.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'dart:core';

class PointsRepository extends GetxController {
  static PointsRepository get instance => Get.find();

  final _db = FirebaseFirestore.instance;

  Future<List<PtsHistoryModel>> getMemberPtsHistory(String memID) async {
    final snapshot = await _db
        .collection("PointsTracking")
        .where("memberID", isEqualTo: memID)
        .orderBy("date", descending: true)
        .get();
    final PtsHistoryData =
        snapshot.docs.map((e) => PtsHistoryModel.fromSnapshot(e)).toList();
    return PtsHistoryData;
  }

  createPoints(int cost, String name, String memID) async {
    final ptsHistoryData = PtsHistoryModel(
        name: "Redeem $name",
        memberID: memID,
        date: Timestamp.fromDate(DateTime.now()),
        pointsDiff: -cost);

    await _db
        .collection("PointsTracking")
        .add(ptsHistoryData.toJson())
        .whenComplete(() => null)
        .catchError((error, StackTrace) {
      Get.snackbar("Error", "Something went wrong. Try again",
          snackPosition: SnackPosition.BOTTOM,
          backgroundColor: Colors.redAccent,
          colorText: Colors.white);
    });
  }
}
