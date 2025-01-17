'use client'


import { useUser, SignedIn, SignedOut, UserButton, SignInButton } from '@clerk/nextjs'
import React from 'react'

function Header() {
    const {user} = useUser();


  return (
    <div className="flex justify-between items-center px-8 py-4">
       {user && (
        <h1>{user?.firstName}{`'s`} Space</h1> 
       )}

       {/* Breadcrumb */}


       {/* SignIn/SignOut Btn */}
       <div>
        
        <SignedOut>
            <SignInButton />
        </SignedOut>

        <SignedIn>
            <UserButton />
        </SignedIn>

       </div>

    </div>
  )
}

export default Header