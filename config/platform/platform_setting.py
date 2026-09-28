class PlatformSetting:

    limit_character = 4000
    limit_file_size = 50000

    def update_limit_file_size(self, limit: int):
        self.limit_file_size = limit

    def update_limit_character(self, limit: int):
        self.limit_character = limit

    def update_time_out(self, time_out: int):
        self.limit_character = time_out
