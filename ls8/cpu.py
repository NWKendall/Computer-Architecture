"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0
        self.reg = [0] * 8
        self.LDI = 0b10000010
        self.PRN = 0b01000111
        self.HLT = 0b00000001
        self.MUL = 0b10100010

    def load(self, program):
        """Load a program into memory."""
        print("working?")
        #    index     value        provide from arg
        for address, instruction in enumerate(program):
            self.ram[address] = instruction
            print(address, bin(instruction))
            address += 1
        # argsv code in here to initiate   
        # recieving input [python3, file_name, args]
            #  split
            # control for strings  
        # # split

    def alu(self, op, reg_a, reg_b):
        """ALU operations.
        Algorythmic Logic Units
        # add masking?
            use repl
        """
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
            
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
            # print("REGISTRY:", self.reg)
            self.pc += 3
            # print("MUL", self.reg[reg_a])
            print(f"MUL at REG[{reg_a}]: {self.reg[reg_a]}")
        else:
            raise Exception(f"Unsupported ALU operation: {op}")
            self.trace()

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU.       
        1. read mem at PC
        2. store result in local var
        3. turn into hash_tables
        """
        running = True
        while running:
            IR = self.ram[self.pc]
            branch_table = {
                self.LDI: self.ldi,
                self.PRN: self.prn,
                # self.HLT: self.hlt,
                self.MUL: self.mul
                }
            if IR in branch_table:
                branch_table[IR]()
            elif IR == self.HLT:
                running = False
            else:
                print(f'Unknown instruction: {IR}, at address PC: {self.pc}')
                sys.exit(1)

    def ram_read(self, address):
        # accept address
        # return it's value
        return self.ram[address]

    def ram_write(self, value, address):
        # take a value
        # write to address
        # no return
        self.ram[address] = value

    def hlt(self, running):
        self.pc += 1
        running = False
        return running
    
    def prn(self):
        reg_id = self.ram[self.pc + 1]
        self.reg[0]
        print("Returning", self.reg[reg_id])
        self.pc +=2
    
    def ldi(self):
        reg_id = self.ram[self.pc + 1]
        value = self.ram[self.pc + 2]
        self.reg[reg_id] = value
        self.pc += 3
    
    def mul(self):
        self.alu("MUL", 0, 1)
