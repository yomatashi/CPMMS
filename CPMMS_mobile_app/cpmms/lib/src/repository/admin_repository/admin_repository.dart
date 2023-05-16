import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:cpmms/src/features/authentications/models/admin_model.dart';
import 'package:get/get.dart';

class AdminRepository extends GetxController{
  static AdminRepository get instance => Get.find();

  final _db = FirebaseFirestore.instance;

  Future<AdminModel> getAdminDetails(String email) async{
    final snapshot = await _db.collection("Admin").where("email", isEqualTo: email).get();
    final adminData = snapshot.docs.map((e) => AdminModel.fromSnapshot(e)).single;
    return adminData;
  }

  Future<List<AdminModel>> allAdmin() async{
    final snapshot = await _db.collection("Admin").get();
    final adminData = snapshot.docs.map((e) => AdminModel.fromSnapshot(e)).toList();
    return adminData;
  }
  
}