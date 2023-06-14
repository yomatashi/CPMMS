import 'package:cloud_firestore/cloud_firestore.dart';

class PtsHistoryModel {
  final String? id;
  final String name;
  final String memberID;
  final Timestamp date;
  final int pointsDiff;

  const PtsHistoryModel({
    this.id,
    required this.name,
    required this.memberID,
    required this.date,
    required this.pointsDiff,
  });

  toJson() {
    return {
      "name": name,
      "memberID": memberID,
      "date": date,
      "pointsDiff": pointsDiff,
    };
  }

  factory PtsHistoryModel.fromSnapshot(
      DocumentSnapshot<Map<String, dynamic>> document) {
    final data = document.data()!;
    return PtsHistoryModel(
        id: document.id,
        name: data["name"],
        memberID: data["memberID"],
        date: data["date"],
        pointsDiff: data["pointsDiff"].toInt());
  }
}
