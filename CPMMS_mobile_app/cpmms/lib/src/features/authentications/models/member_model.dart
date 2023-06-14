import 'package:cloud_firestore/cloud_firestore.dart';

class MemberModel {
  final String id;
  final String fullName;
  final String email;
  final String IC;
  final int points;
  final String pfp;

  const MemberModel({
    required this.id,
    required this.fullName,
    required this.email,
    required this.IC,
    required this.points,
    required this.pfp,
  });

  toJson() {
    return {
      "fullName": fullName,
      "email": email,
      "IC": IC,
      "points": points,
      "pfp": pfp,
    };
  }

  factory MemberModel.fromSnapshot(
      DocumentSnapshot<Map<String, dynamic>> document) {
    final data = document.data()!;
    return MemberModel(
        id: document.id,
        fullName: data["fullName"],
        email: data["email"],
        IC: data["IC"],
        points: data["points"],
        pfp: data["pfp"]);
  }
}
