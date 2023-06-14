import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:cpmms/src/features/core/models/pts_history_model.dart';
import 'package:get/get.dart';

class PointsRepository extends GetxController{
  static PointsRepository get instance => Get.find();

  final _db = FirebaseFirestore.instance;

  Future<List<PtsHistoryModel>> getMemberPtsHistory(String memID) async{
    final snapshot = await _db.collection("PointsTracking").where("memberID", isEqualTo: memID).orderBy("date", descending: true).get();
    final PtsHistoryData = snapshot.docs.map((e) => PtsHistoryModel.fromSnapshot(e)).toList();
    return PtsHistoryData;
  }
  
}