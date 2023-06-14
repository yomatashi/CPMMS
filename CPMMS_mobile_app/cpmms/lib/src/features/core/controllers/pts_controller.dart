import 'dart:io';
import 'package:flutter/material.dart';
import 'package:cpmms/src/repository/member_pts_repository/pts_repository.dart';
import 'package:cpmms/src/features/core/models/pts_history_model.dart';
import 'package:get/get.dart';

class PointsHistoryController extends GetxController {
  static PointsHistoryController get instance => Get.find();

  final _ptsHistoryRepo = Get.put(PointsRepository());

  RxList<PtsHistoryModel> ptsHistoryData = RxList<PtsHistoryModel>();

  Future<void> getPtsHistory(String memID) async{
    final data = await _ptsHistoryRepo.getMemberPtsHistory(memID);
    ptsHistoryData.value = data;
  }
}