import 'package:cloud_firestore/cloud_firestore.dart';

class ClaimRewardsModel{
  String id;
  final bool claimStatus;
  final String memberID;
  final String rewardsID;

  ClaimRewardsModel({
    required this.id,
    required this.claimStatus,
    required this.memberID,
    required this.rewardsID,
  });

  toJson() {
    return {
      "claimStatus": claimStatus,
      "memberID": memberID,
      "rewardsID": rewardsID,
    };
  }

  factory ClaimRewardsModel.fromSnapshot(
      DocumentSnapshot<Map<String, dynamic>> document) {
    final data = document.data()!;
    return ClaimRewardsModel(
        id: document.id,
        claimStatus: data["claimStatus"],
        memberID: data["memberID"],
        rewardsID: data["rewardsID"]);
  }
}