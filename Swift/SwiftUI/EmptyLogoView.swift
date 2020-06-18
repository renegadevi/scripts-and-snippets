//
//  EmptyLogoView.swift
//
//  Created by Philip Andersen on 2020-02-01.
//  Copyright © 2020 Philip Andersen. All rights reserved.
//

import SwiftUI

struct EmptyLogoView: View {
    
    var body: some View {
            
        GeometryReader { geometry in
            
            List{
                
                Section(header: VStack {
                    
                    self.padding(.top, (geometry.size.height/2.6))
                    
                    Image("app_logo")  // your asset name
                        .resizable(resizingMode: .stretch)
                        .antialiased(true)
                        .aspectRatio(contentMode: .fit)
                        .frame(maxWidth: 400, maxHeight: 200)
                        .opacity(0.35)
                    
                }) { EmptyView() }
            }
            .listStyle(GroupedListStyle())
    
        }
    
    }
    
}

        
        
