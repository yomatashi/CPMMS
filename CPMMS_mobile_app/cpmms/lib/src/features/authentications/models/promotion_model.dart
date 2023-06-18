import 'package:cloud_firestore/cloud_firestore.dart';

class PromotionModel{
  String id;
  final String promotionName;
  final String details;
  String img;

  PromotionModel({
    required this.id,
    required this.promotionName,
    required this.details,
    required this.img,
  });

  toJson() {
    return {
      "promotionName": promotionName,
      "details": details,
      "img": img,
    };
  }

  factory PromotionModel.fromSnapshot(
      DocumentSnapshot<Map<String, dynamic>> document) {
    final data = document.data()!;
    return PromotionModel(
        id: document.id,
        promotionName: data["promotionName"],
        details: data["details"],
        img: data["img"]);
  }
}