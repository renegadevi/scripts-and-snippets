//
// SettingsResetButton.swift
//
// Example of an reset button you may see at the bottom of
// settings view.
//
// Note:
// - Tested using Xcode 11.0 beta 6 on MacOS Mojave 10.14.5


struct SettingsView: View {

    // We use this as a change of action
    @State var resetAlert: Bool = false


    var body: some View {


        // We first have a list, and usually this is a grouped list style in
        // order to create separation.
        List {

            // ... section1

            // ... section2

            // ... section3


            // MARK:- Reset all settings to default

            // We make it a separate section at the bottom so it's clear to the
            // user it's not part of the rest and to follow the iOS native
            // looking guidelines in apps
            Section {

                // We create a button
                Button(action: {

                    // When the user calls to action, we toggle the state value
                    self.resetAlert.toggle()

                }) {

                    // Create a button of the whole list cell and make it red
                    // and centered.
                    Text("Reset all settings to default")
                        .foregroundColor(.red)
                        .frame(minWidth: 0, maxWidth: .infinity, alignment: .center)
                }

                // We create a alert to the user to confirm so no accidental
                // inputs is made.
                //
                // This can be remade into a actionsheet, where a menu pops up
                // from the bottom. As I was troubleshooting it broke for me
                // in the lastest betas, where's Alert is stable and just works.
                .alert(isPresented:$resetAlert) {
                    Alert(
                        title: Text("Are you sure you want to reset all settings?"),
                        message: Text("This will restore all settings to default values. Saved data in the app will not be affected."),
                        primaryButton: .destructive(Text("Reset")) {
                            // Call to reset function
                            NSLog("Resetting Settings to default values.")
                        },
                        secondaryButton: .cancel()
                    )
                }
            }

        }.listStyle(GroupedListStyle())

    }
}
