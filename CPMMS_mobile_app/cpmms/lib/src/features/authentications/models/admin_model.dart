import 'package:cloud_firestore/cloud_firestore.dart';

class AdminModel {
  final String? id;
  final String fullName;
  final String email;
  final String position;

  const AdminModel({
    this.id,
    required this.fullName,
    required this.email,
    required this.position,
  });

  toJson() {
    return {
      "fullName": fullName,
      "email": email,
      "position": position,
    };
  }

  factory AdminModel.fromSnapshot(
      DocumentSnapshot<Map<String, dynamic>> document) {
    final data = document.data()!;
    return AdminModel(
        id: document.id,
        fullName: data["fullName"],
        email: data["email"],
        position: data["position"]);
  }
}
