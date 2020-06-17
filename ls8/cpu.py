"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0
        self.reg = [0] * 8
        self.running = True
        self.LDI = 0b10000010
        self.PRN = 0b01000111
        self.HLT = 0b00000001
        self.ADD = 0b10100000
        self.MUL = 0b10100010

    def load(self, program):
        """Load a program into memory."""
        #    index     value        provide from arg
        for address, instruction in enumerate(program):
            self.ram[address] = instruction
            address += 1

    def run(self):
        """Run the CPU.       
        1. read mem at PC
        2. store result in local var
        3. turn into hash_tables
        """
        
        while self.running is True:
            IR = self.ram[self.pc]
            branch_table = {
                self.LDI: self.ldi,
                self.PRN: self.prn,
                self.HLT: self.hlt,
                self.ADD: self.add,
                self.MUL: self.mul,
                }
            if IR in branch_table:
                branch_table[IR]()
            else:
                print(f'Unknown instruction: {IR}, at address PC: {self.pc}')
                sys.exit(1)
            # branch_table.get(IR)()

    def alu(self, op, reg_a, reg_b):
        """ALU operations.
        Algorythmic Logic Units
        # add masking?
            use repl
        """
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
            self.pc += 3
            print(f"MUL at REG[{reg_a}]: {self.reg[reg_a]}")
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


    def ram_read(self, address):
        # accept address
        # return it's value
        return self.ram[address]

    def ram_write(self, value, address):
        # take a value
        # write to address
        # no return
        self.ram[address] = value

    def hlt(self):
        self.running = False
        self.pc += 1

    
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

    def add(self):
        self.alu("ADD", 0, 1)
        
    def mul(self):
        self.alu("MUL", 0, 1)
