import 'package:cpmms/src/features/authentications/models/member_model.dart';
import 'package:cpmms/src/repository/admin_repository/admin_repository.dart';
import 'package:cpmms/src/repository/authentication_repository/authentication_repository.dart';
import 'package:cpmms/src/repository/member_repository/member_repository.dart';
import 'package:get/get.dart';

class DashboardController extends GetxController{
  static DashboardController get instance => Get.find();

  final _authRepo = Get.put(AuthenticationRepository());
  final _memberRepo = Get.put(MemberRepository());
  final _adminRepo = Get.put(AdminRepository());

  getMemberData() async{
    final email = _authRepo.firebaseUser.value?.email;
    if(email != null){
      return _memberRepo.getMemberDetails(email);
    }else{
      Get.snackbar("Error", "Login to continue");
    }
  } 

  getAdminData(){
    final email = _authRepo.firebaseUser.value?.email;
    if(email != null){
      return _adminRepo.getAdminDetails(email);
    }else{
      Get.snackbar("Error", "Login to continue");
    }
  }

  updateMember(MemberModel member) async{
    await _memberRepo.updateMember(member);
    Get.find<DashboardController>().getMemberData();
  }
}