import 'package:cpmms/src/constants/colors.dart';
import 'package:cpmms/src/constants/image_strings.dart';
import 'package:cpmms/src/constants/sizes.dart';
import 'package:cpmms/src/features/authentications/models/member_model.dart';
import 'package:cpmms/src/features/core/controllers/profile_controller.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import 'package:line_awesome_flutter/line_awesome_flutter.dart';

class UpdateProfileScreen extends StatelessWidget {
  const UpdateProfileScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final controller = Get.put(ProfileController());
    controller.getMemberDataFuture();
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            Get.back();
          },
          icon: const Icon(LineAwesomeIcons.angle_left, color: Colors.black54),
        ),
        title: Text(
          "Edit Profile",
          style: Theme.of(context).textTheme.headlineMedium,
        ),
        centerTitle: true,
        elevation: 0,
        backgroundColor: Colors.transparent,
      ),
      body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.all(tDefaultSize),
          child: FutureBuilder(
            future: controller.getMemberData(),
            builder: ((context, snapshot) {
              if (snapshot.connectionState == ConnectionState.done) {
                if (snapshot.hasData) {
                  MemberModel memberData = snapshot.data as MemberModel;
                  final _formKey = GlobalKey<FormState>();
                  final fullName =
                      TextEditingController(text: memberData.fullName);
                  final email = TextEditingController(text: memberData.email);
                  final IC = TextEditingController(text: memberData.IC);
                  return Column(children: [
                    const SizedBox(height: 10),
                    Form(
                      key: _formKey,
                        child: Column(
                      children: [
                        Stack(children: [
                          SizedBox(
                            width: 120,
                            height: 120,
                            child: ClipRRect(
                              borderRadius: BorderRadius.circular(100),
                              child: controller.imageUrl.value != "none" ? Image.network(controller.imageUrl.value) : Image.asset(tDefaultPfp),
                            ),
                          ),
                          Positioned(
                            bottom: 0,
                            right: 0,
                            child: InkWell(
                              onTap: () {
                                controller.pickAndUploadImage(memberData.id!);
                              },
                              child: Container(
                                width: 35,
                                height: 35,
                                decoration: BoxDecoration(
                                  borderRadius: BorderRadius.circular(100),
                                  color: tPrimaryColor,
                                ),
                                child: const Icon(
                                  LineAwesomeIcons.alternate_pencil,
                                  size: 20,
                                  color: Colors.black,
                                ),
                              ),
                            ),
                          )
                        ]),
                        const SizedBox(height: 50),
                        TextFormField(
                          controller: fullName,
                          decoration: InputDecoration(
                            label: const Text("Full Name"),
                            border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(100)),
                            focusedBorder: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(100),
                                borderSide: const BorderSide(
                                    width: 2, color: tSecondaryColor)),
                            prefixIcon: const Icon(LineAwesomeIcons.user),
                          ),
                        ),
                        const SizedBox(height: tFormHeight - 20),
                        TextFormField(
                          controller: email,
                          enabled: false,
                          decoration: InputDecoration(
                            label: const Text("E-Mail"),
                            border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(100)),
                            focusedBorder: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(100),
                                borderSide: const BorderSide(
                                    width: 2, color: tSecondaryColor)),
                            prefixIcon: const Icon(LineAwesomeIcons.envelope_1),
                          ),
                        ),
                        const SizedBox(height: tFormHeight - 20),
                        TextFormField(
                          inputFormatters: [
                            FilteringTextInputFormatter.digitsOnly,
                            LengthLimitingTextInputFormatter(12)
                          ],
                          validator: (value) {
                            if (value == null || value.isEmpty) {
                              return 'Please enter a value';
                            }
                            if (value.length != 12) {
                              return 'Please enter a 12-digit number for IC numbers';
                            }
                            return null; // Return null if the input is valid
                          },
                          controller: IC,
                          decoration: InputDecoration(
                            label: const Text("IC number"),
                            border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(100)),
                            focusedBorder: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(100),
                                borderSide: const BorderSide(
                                    width: 2, color: tSecondaryColor)),
                            prefixIcon: const Icon(
                                LineAwesomeIcons.identification_card_1),
                          ),
                        ),
                        const SizedBox(height: tFormHeight),
                        SizedBox(
                          width: double.infinity,
                          child: ElevatedButton(
                            onPressed: () async {
                              if (_formKey.currentState!.validate()) {
                                final newMemberData = MemberModel(
                                    id: memberData.id,
                                    fullName: fullName.text.trim(),
                                    email: email.text.trim(),
                                    IC: IC.text.trim(),
                                    points: memberData.points,
                                    pfp: memberData.pfp);

                                await controller.updateMember(newMemberData);
                              }
                            },
                            style: ElevatedButton.styleFrom(
                                backgroundColor: tPrimaryColor,
                                side: BorderSide.none,
                                shape: const StadiumBorder()),
                            child: const Text(
                              "Update Profile",
                              style: TextStyle(color: tDarkColor),
                            ),
                          ),
                        ),
                      ],
                    ))
                  ]);
                } else if (snapshot.hasError) {
                  return Center(child: Text(snapshot.error.toString()));
                } else {
                  return const Center(child: Text("Something went wrong"));
                }
              } else {
                return const Center(child: CircularProgressIndicator());
              }
            }),
          ),
        ),
      ),
    );
  }
}
