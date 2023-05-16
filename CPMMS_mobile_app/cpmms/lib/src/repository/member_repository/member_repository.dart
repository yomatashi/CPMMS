import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:cpmms/src/features/authentications/models/member_model.dart';
import 'package:get/get.dart';

class MemberRepository extends GetxController{
  static MemberRepository get instance => Get.find();

  final _db = FirebaseFirestore.instance;

  Future<MemberModel> getMemberDetails(String email) async{
    final snapshot = await _db.collection("Member").where("email", isEqualTo: email).get();
    final memberData = snapshot.docs.map((e) => MemberModel.fromSnapshot(e)).single;
    return memberData;
  }

  Future<List<MemberModel>> allMember() async{
    final snapshot = await _db.collection("Member").get();
    final memberData = snapshot.docs.map((e) => MemberModel.fromSnapshot(e)).toList();
    return memberData;
  }
  
}