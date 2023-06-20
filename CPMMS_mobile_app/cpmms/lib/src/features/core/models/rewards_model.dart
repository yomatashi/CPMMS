import 'package:cloud_firestore/cloud_firestore.dart';

class RewardsModel{
  String id;
  final int cost;
  final String details;
  final String instruction;
  String img;

  RewardsModel({
    required this.id,
    required this.cost,
    required this.details,
    required this.instruction,
    required this.img,
  });

  toJson() {
    return {
      "cost": cost,
      "details": details,
      "instruction": instruction,
      "img": img,

    };
  }

  factory RewardsModel.fromSnapshot(
      DocumentSnapshot<Map<String, dynamic>> document) {
    final data = document.data()!;
    return RewardsModel(
        id: document.id,
        cost: data["cost"],
        details: data["details"],
        instruction: data["instruction"],
        img: data["img"]);
  }
}