import React from 'react'
import NewDocumentBtn from './NewDocumentBtn'
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"
import { MenuIcon } from 'lucide-react'


function Sidebar() {
  return (
    <div className=" bg-gray-200 p-2 md:p-5 relative">

      {/* Only Sheet for Mobile */}
      <div className='md:hidden inline'>
      <Sheet >
        <SheetTrigger><MenuIcon className='hover:opacity-30 rounded-lg' size={30} /></SheetTrigger>
        <SheetContent side='left'>
          {/* Content should be Centered */}
            <SheetHeader>
            <div className='flex justify-center  h-full'>
                <SheetTitle>Menu</SheetTitle>
                
            </div>
            </SheetHeader>
            {/* Options will be there */}
            <div className='flex flex-col items-center h-full'><NewDocumentBtn /></div>
        </SheetContent>
      </Sheet>

      </div>
      



      <div className='hidden md:inline'>
        <NewDocumentBtn />
      </div>
    </div>
  )
}

export default Sidebar