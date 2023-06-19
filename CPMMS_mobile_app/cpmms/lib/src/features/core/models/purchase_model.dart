import 'package:cloud_firestore/cloud_firestore.dart';

class PurchaseModel{
  final String? id;
  final String memberID;
  final String paymentMode;
  final double totalPrice;
  final Timestamp date;
  final List items;

  const PurchaseModel({
    this.id,
    required this.memberID,
    required this.paymentMode,
    required this.totalPrice,
    required this.date,
    required this.items
  });

  toJson() {
    return {
      "memberID": memberID,
      "paymentMode": paymentMode,
      "totalPrice": totalPrice,
      "date": date,
      "items": items,

    };
  }

  factory PurchaseModel.fromSnapshot(
      DocumentSnapshot<Map<String, dynamic>> document) {
    final data = document.data()!;
    return PurchaseModel(
        id: document.id,
        memberID: data["memberID"],
        paymentMode: data["paymentMode"],
        totalPrice: data["totalPrice"],
        date: data["date"],
        items: data["items"]);
  }
}